"""
@version: 1.0.0
@author: wangke
@time: 2018/9/24 下午1:33
@contact: merpyzf@qq.com
@software: PyCharm
"""


class BookViewModel:
    @classmethod
    def package_single(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = 1
            returned['books'] = [cls.__cut_book_data(data)]
        return returned

    @classmethod
    def package_collection(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = data['total']
            # Python列表推导式
            returned['books'] = [cls.__cut_book_data(book) for book in data['books']]
        return returned

    @classmethod
    def __cut_book_data(cls, data):
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'pages': data['pages'] or '', # 如果获取到的值为none则将其使用空字符串替代
            'author': '、'.join(data['author']),
            'summary': data['summary'] or '',
            'image': data['image']
        }
        return book
