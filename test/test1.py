"""
@version: 1.0.0
@author: wangke
@time: 2018/9/21 下午10:30
@contact: merpyzf@qq.com
@software: PyCharm
"""


class SQLManager:
    def __enter__(self):
        print('__enter__方法执行了')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__方法执行了，进行资源释放')

    def touch_except(self):
        print('生成一个除0异常')
        a = 1 / 0

if __name__ == '__main__':

    with SQLManager() as manager:
        print("hihihi")