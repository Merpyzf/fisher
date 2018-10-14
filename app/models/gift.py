"""
@version: 1.0.0
@author: wangke
@time: 2018/9/30 9:26 PM
@contact: merpyzf@qq.com
@software: PyCharm
"""
from sqlalchemy import Column, Integer, Boolean, ForeignKey, String,desc
from sqlalchemy.orm import relationship
from app.models.base import Base
from flask import current_app
from app.spider.yushu_book import YuShuBook
class Gift(Base):
    id = Column(Integer, primary_key=True)
    # 与User模型相关联
    user = relationship('User')
    uid = Column(Integer,ForeignKey('user.id'))
    # 标识书籍是否赠出
    launched = Column(Boolean, default=False)
    # 不同的用户可能赠送出同一本书籍，因此isbn编号可以存在重复
    isbn = Column(String(15),nullable=False)
    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first


    # 论将recent方法修改成类方法的合理性，一个Gift对象实例仅表示一个礼物，而在这个仅表示一个礼物的对象中
    # 又可以查询多条书籍的信息，显然不合适。违背面向对象的思想
    @classmethod
    def recent(self):
        # 查询前30条最近赠送的书籍信息，先将查询到的所有赠送的数据（未赠出）排序，然后在取30条数据，这里
        # 需要注意limit和order_by的顺序，应该先排序再使用limit从中取数据
        # distinct用于实现去重操作，在去重前需要先根据能够区别图书的isbn编号先进行分组操作
        # 链式调用,当调用all()或者first()方法才会去执行sql查询的操作
        # desc()倒叙
        return Gift.query.filter_by(launched = False).group_by(
            Gift.isbn).order_by(
            desc(Gift.create_time)).limit(
            current_app.config['RECENT_BOOK_COUNT']).distinct().all()

