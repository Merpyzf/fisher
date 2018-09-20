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


@web.route('/book/search')
def search():
    """
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
        if isbn_or_key == 'key':
            result = YuShuBook.search_by_key(q, page)
        else:
            result = YuShuBook.search_by_isbn(q)
        return jsonify(result)
    else:
        return jsonify(form.errors)