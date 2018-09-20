"""
@version: 1.0
@author: wangke
@time: 2018/9/19 下午7:16
@contact: merpyzf@qq.com
@software: PyCharm
"""

def is_isbn_or_key(q):
    """
    判断用户搜索的关键字是isbn还是书籍名称信息
    :param q:
    :return:
    """
    # isbn13由13个0到9的数字组成
    # isbn10由 10个0到9的数字组成，并且其中含有一些' - '
    isbn_or_key = 'key'
    if len(q) == 13 and q.isdigit():
        isbn_or_key = 'isbn'
    short_q = q.replace('-', '')
    if '-' in q and len(short_q) == 10 and short_q.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key
