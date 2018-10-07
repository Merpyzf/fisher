"""
@version: 1.0.0
@author: wangke
@time: 2018/9/30 9:26 PM
@contact: merpyzf@qq.com
@software: PyCharm
"""
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.base import Base
from sqlalchemy import Column, Integer,String,Boolean,Float
from flask_login import UserMixin
from app import  login_manager

class User(UserMixin, Base):
    # 为User模型在数据库对应的表指定别名
    # __tablename__ ='user1'
    # 设置主键id
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    _password = Column('password', String(128), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))
    # 读取属性
    @property
    def password(self):
        return self._password
    # 属性写入
    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        print(check_password_hash(self._password, raw))
        return check_password_hash(self._password,raw)

    def get_id(self):
        return self.id

@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))
