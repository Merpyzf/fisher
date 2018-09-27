"""
@version: 1.0.0
@author: wangke
@time: 2018/9/20 上午9:21
@contact: merpyzf@qq.com
@software: PyCharm
"""
import json

from flask import jsonify, request, render_template

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
        # Python建议在合适的位置使用空行来分割代码片段，使得代码变得更加易读
        if isbn_or_key == 'key':
            yushuBook.search_by_key(keyword=q, page=page)
        else:
            yushuBook.search_by_isbn(q)
        books.fill(yushuBook, q)
        return json.dumps(books, default=lambda o: o.__dict__)
    else:
        return jsonify(form.errors)


@web.route('/test')
def test():
    r = {
        'name': '春水碧于天',
        'age': '18'
    }
    return render_template('test_extend.html', data=r)
