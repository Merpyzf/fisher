"""
@version: 1.0.0
@author: wangke
@time: 2018/9/30 9:26 PM
@contact: merpyzf@qq.com
@software: PyCharm
"""
from sqlalchemy import Column, Integer, Boolean, ForeignKey, String
from sqlalchemy.orm import relationship
from app.models.base import Base

class Gift(Base):
    id = Column(Integer, primary_key=True)
    # 与User模型相关联
    user = relationship('User')
    uid = Column(Integer,ForeignKey('user.id'))
    # 标识书籍是否赠出
    launched = Column(Boolean, default=False)
    # 不同的用户可能赠送出同一本书籍，因此isbn编号可以存在重复
    isbn = Column(String(15),nullable=False)
