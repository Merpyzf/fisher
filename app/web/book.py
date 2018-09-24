"""
@version: 1.0.0
@author: wangke
@time: 2018/9/20 上午9:21
@contact: merpyzf@qq.com
@software: PyCharm
"""
from flask import jsonify, request

from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.web import web
from app.view_models.book import BookViewModel, BookCollection


@web.route('/book/search')
def search():
    """
    用于对书籍进行搜索的视图函数
    :param q: 图书搜索关键字
    :param page:  页数
    :return:
    """
    form = SearchForm(request.args)
    if form.validate():
        # 调用strip()函数去除前后的空格
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        books = BookCollection()
        yushuBook = YuShuBook()
        if isbn_or_key == 'key':
            yushuBook.search_by_key(keyword=q, page=page)
        else:
            yushuBook.search_by_isbn(q)
        books.fill(yushuBook, q)
        return jsonify(books)
    else:
        return jsonify(form.errors)
