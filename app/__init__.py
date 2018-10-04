"""
@version: 1.0.0
@author: wangke
@time: 2018/9/20 上午10:00
@contact: merpyzf@qq.com
@software: PyCharm
"""
from flask import Flask
from flask_login import LoginManager
from app.models.base import db

login_manager = LoginManager()

def create_app():
    # __name__ 决定了项目的根目录
    # 默认静态资源存放的文件夹为应用根目录下的static目录下，可以通过传入静态文件夹路径的方式来自定义的指定静态资源文件夹放置的位置
    app = Flask(__name__, static_folder='static', static_url_path='/s')
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)
    # 将插件注册到核心对象中
    login_manager.init_app(app)
    # 注册数据库
    db.init_app(app)
    with app.app_context():
        # 生成表
        db.create_all()
    # db.create_all(app)
    return app

def register_blueprint(app):
    from app.web.book import web
    # 给app注册一个蓝图
    app.register_blueprint(web)
