"""
@version: 1.0.0
@author: wangke
@time: 2018/9/21 下午10:30
@contact: merpyzf@qq.com
@software: PyCharm
"""

from werkzeug.local import LocalStack
import threading
import time
s = LocalStack()
s.push('1')
s.push('2')

def worker():
    s.push('3')
    print(s)
    print(s.top)
    s.pop()
    print(s.top)



t = threading.Thread(target=worker)
t.start()
time.sleep(1)

print("main --> "+s.top)


