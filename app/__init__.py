"""
@version: 1.0.0
@author: wangke
@time: 2018/9/20 上午10:00
@contact: merpyzf@qq.com
@software: PyCharm
"""
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)
    return app

def register_blueprint(app):
    from app.web.book import web
    # 给app注册一个蓝图
    app.register_blueprint(web)
