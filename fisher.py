from flask import Flask, make_response
from helper import is_isbn_or_key

app = Flask(__name__)
app.config.from_object('config')


@app.route('/book/search/<q>/<page>')
def search(q, page):
    """
    :param q: 图书搜索关键字
    :param page:  页数
    :return:
    """
    isbn_or_key = is_isbn_or_key(q)


if __name__ == '__main__':
    # 开启flask的debug模式，当程序发生改动时候，flask框架会监听改动并自动重启服务器
    # 开启debug模式后也可以把详细的错误信息显示在网页当中
    app.run("0.0.0.0", debug=app.config['DEBUG'])
