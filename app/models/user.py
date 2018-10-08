"""
@version: 1.0.0
@author: wangke
@time: 2018/9/30 9:26 PM
@contact: merpyzf@qq.com
@software: PyCharm
"""
from werkzeug.security import generate_password_hash, check_password_hash

from app.libs.helper import is_isbn_or_key
from app.models.base import Base
from sqlalchemy import Column, Integer,String,Boolean,Float
from flask_login import UserMixin
from app import login_manager
from app.models.gift import Gift
from app.models.wish import Wish
from app.spider.yushu_book import YuShuBook


class User(UserMixin, Base):
    # 为User模型在数据库对应的表指定别名
    # __tablename__ ='user1'
    # 设置主键id
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    beans = Column(Float, default=0)
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
    #  判断传入的isbn编号是否可以被用户赠送
    def can_save_to_list(self, isbn):
        # 验证isbn编号的正确性
        if is_isbn_or_key(isbn) !='isbn':
            return False
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(isbn)
        # 从api中查找传入的isbn编号，确定isbn对应的书籍在api中存在
        if not yushu_book.first:
            return False
        # 不允许用户同时赠送多本相同的数
        # 一个用户不可能同时成为赠送者和索要者
        # 获取当前用户下面正在赠送的书籍
        gifting = Gift.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()
        wishing = Wish.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()
        # 此处判断用户是否同有在同时赠送一本的逻辑可能存在问题，待验证
        if not gifting and not wishing:
            return True
        else:
            return False



@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))
