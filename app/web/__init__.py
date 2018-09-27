"""
@version: 1.0.0
@author: wangke
@time: 2018/9/20 上午10:01
@contact: merpyzf@qq.com
@software: PyCharm
"""
from flask import Blueprint

web = Blueprint('web', __name__, template_folder='templates')
from app.web import book
