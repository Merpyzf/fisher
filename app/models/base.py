"""
@version: 1.0.0
@author: wangke
@time: 2018/9/30 9:27 PM
@contact: merpyzf@qq.com
@software: PyCharm
"""
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from sqlalchemy import Column, Integer, SmallInteger
from contextlib import contextmanager
from datetime import datetime
class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            # 抛出异常
            raise e

db = SQLAlchemy()
class Base(db.Model):
    # 添加 __abstract__ = True 标识SQLAlchemy不要创建一个表名为Base的表，如果不添加会提示缺少主键的错误
    __abstract__ = True
    # create_time = Column('create_time', Integer)
    # 记录数据状态,1表示数据存在
    status = Column(SmallInteger, default=1)
    create_time = Column('create_time', Integer)
    def __init__(self):
        self.create_time = int(datetime.now().timestamp())

    # 根据表单传入的字典参数来完成数据的自动赋值
    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            # 判断当前对象中是否包含名字为key的属性
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)
    @property
    def create_datetime(self):
        # 将int类型的时间戳转换成datetime类型
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return