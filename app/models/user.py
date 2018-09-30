"""
@version: 1.0.0
@author: wangke
@time: 2018/9/30 9:26 PM
@contact: merpyzf@qq.com
@software: PyCharm
"""
from app import db
from sqlalchemy import Column, Integer,String,Boolean,Float

class User(db.Model):
    # 设置主键id
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))