"""
@version: 1.0.0
@author: wangke
@time: 2018/10/2 5:00 PM
@contact: merpyzf@qq.com
@software: PyCharm
"""
class Person():
    def __init__(self, name, age):
        print('Base类的__init__方法执行了')

class Student(Person):
    pass

if __name__ =='__main__':
    # 当一个类继承自一个父类时，如果子类没有构造方法的话则会默认调用父类的构造方法
    s = Student('wangke', 19)
