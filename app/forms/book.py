"""
表单验证器
@version: 1.0.0
@author: wangke
@time: 2018/9/20 下午6:56
@contact: merpyzf@qq.com
@software: PyCharm
"""

from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired


class SearchForm(Form):
    # 增加一个数据不能为空的验证
    q = StringField(validators=[DataRequired(),Length(min=1, max=30,message='查询关键字的长度要在1-30个字符之间')])
    # 可以指定一个默认值
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
