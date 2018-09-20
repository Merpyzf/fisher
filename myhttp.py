"""
@version: 1.0.0
@author: wangke
@time: 2018/9/19 下午8:49
@contact: merpyzf@qq.com
@software: PyCharm
"""
import requests


class HTTP:
    def __init__(self):
        pass
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        else:
            return r.json() if return_json else r.text

if __name__ == '__main__':
    result = HTTP.get('http://t.yushu.im/v2/book/isbn/9787115216878')
    print(type(result))