"""
@version: 1.0.0
@author: wangke
@time: 2018/9/21 下午9:25
@contact: merpyzf@qq.com
@software: PyCharm
"""

from flask import Flask, current_app

app = Flask(__name__)
app.app_context()

@app.route('/test')
def test():

    a = current_app
    d = current_app.config['DEBUG']
    return "hihi"


if __name__ == '__main__':
    app.run('0.0.0.0', 5555, debug=True)
