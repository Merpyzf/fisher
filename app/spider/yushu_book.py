"""
@version: 1.0.0
@author: wangke
@time: 2018/9/19 下午10:36
@contact: merpyzf@qq.com
@software: PyCharm
"""
from flask import current_app

from app.libs.myhttp import HTTP


class YuShuBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{q}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={q}&count={count}&start={start}'

    def __init__(self):
        self.total = 0
        self.books = []

    def search_by_key(self, keyword, page):
        keyword_url = self.keyword_url.format(q=keyword, count=current_app.config['PER_PAGE'],
                                              start=self.calculate_start(page))
        result = HTTP.get(keyword_url)
        # 将获取到的数据存储到对象的实例对象中而不是直接返回给外部调用处
        self.__fill_collection(result)

    def search_by_isbn(self, q):
        isbn_url = self.isbn_url.format(q=q)
        print(isbn_url)
        result = HTTP.get(isbn_url)
        #  将获取到的数据存储到对象的实例对象中而不是直接返回给外部调用处
        self.__fill_single(result)

    def __fill_single(self, data):
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_collection(self, data):
        self.total = data['total']
        self.books = data['books']

    def calculate_start(self, page):
        start = (page - 1) * current_app.config['PER_PAGE']
        return start

    @property
    def first(self):
        # 封装一个first方法后调用者无需知道第一本书在集合中的位置也可以方便调用
        return self.books[0] if len(self.books) >= 0 else None
