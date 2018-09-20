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
    per_page = 15

    @classmethod
    def search_by_key(cls, keyword, page):
        keyword_url = cls.keyword_url.format(q=keyword, count=current_app.config['PER_PAGE'],
                                             start=cls.calculate_start(page))
        result = HTTP.get(keyword_url)
        return result

    @classmethod
    def search_by_isbn(cls, q):
        isbn_url = cls.isbn_url.format(q=q)
        print(isbn_url)
        result = HTTP.get(isbn_url)
        return result

    @staticmethod
    def calculate_start(page):
        start = (page - 1) * current_app.config['PER_PAGE']
        return start
