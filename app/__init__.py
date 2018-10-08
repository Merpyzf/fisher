"""
@version: 1.0.0
@author: wangke
@time: 2018/9/20 上午10:00
@contact: merpyzf@qq.com
@software: PyCharm
"""
from flask import Flask
from flask_script import Manager
from flask_login import LoginManager
from app.models.base import db
from flask_migrate import Migrate, MigrateCommand
login_manager = LoginManager()
# 引入需要迁移的数据库模型
from app.models.user import User
from app.models.gift import Gift
from app.models.wish import Wish
from app.models.book import Book




def create_app():
    # __name__ 决定了项目的根目录
    # 默认静态资源存放的文件夹为应用根目录下的static目录下，可以通过传入静态文件夹路径的方式来自定义的指定静态资源文件夹放置的位置
    app = Flask(__name__, static_folder='static', static_url_path='/s')
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)
    # 将插件注册到核心对象中
    login_manager.init_app(app)
    # 告知login_manage视图函数位置
    login_manager.login_view = 'web.login'
    # 当未登录状态时跳转到登录页面的flash的消息提示
    login_manager.login_message = '请先登录或注册'
    # 注册数据库
    db.init_app(app)

    # 数据库迁移更新管理
    migrate = Migrate(app, db)
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)
    # 当数据模型修改时需要更新数据库，则取消下面的注释，执行
    # python fisher.py db upgrade 命令
    if app.config['NEED_DB_MIGRATE']:
         manager.run()

    with app.app_context():
        # 生成表
        db.create_all()
    # db.create_all(app)
    return app

def register_blueprint(app):
    from app.web.book import web
    # 给app注册一个蓝图
    app.register_blueprint(web)
