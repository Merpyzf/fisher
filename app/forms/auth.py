"""
@version: 1.0.0
@author: wangke
@time: 2018/10/2 5:20 PM
@contact: merpyzf@qq.com
@software: PyCharm
"""
from wtforms import Form, StringField,PasswordField
from wtforms.validators import DataRequired, Length, Email, ValidationError

from app.models.user import User


class RegisterForm(Form):
    email = StringField(validators=[DataRequired(),Length(8,64),
                            Email(message='电子邮箱不符合规范')])
    password = PasswordField(validators=[DataRequired(message='密码不可以为空，请输入你的密码'), Length(6, 32)])
    nickname = StringField(validators=[DataRequired(), Length(2,10, message='昵称输入最少需要2个字符，最多10个字符')])

    # 自定义验证器，书写规则必须以validate开头下划线后面指定需要进行验证的字段
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮件已被注册！')
    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('昵称已被占用！')
