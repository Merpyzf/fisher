"""
@version: 1.0.0
@author: wangke
@time: 2018/9/20 下午10:27
@contact: merpyzf@qq.com
@software: PyCharm
"""
from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Book(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), default='无名')
    binding = Column(String(20))
    price = Column(String(20))
    pubdate = Column(String(20))
    isbn = Column(String(15),nullable=False, unique=True)
    summary =Column(String(1000))
    image = Column(String(50))


    def sample(self):
        pass
