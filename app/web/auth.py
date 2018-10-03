from flask import render_template, request

from app import db
from app.models.user import User
from app.forms.auth import RegisterForm

from . import web

__author__ = '七月'


@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    # 验证用户提交的表单数据
    if request.method == 'POST' and form.validate():
        user = User()
        # form.data获取客户端提交的字典类型的参数
        user.set_attrs(form.data)
        # 将数据存储到数据库中
        db.session.add(user)
        db.session.commit()
    # form.errors 以字典的形式存放表单的验证信息
    # print(form.errors)
    return render_template('auth/register.html',form=form)

@web.route('/login', methods=['GET', 'POST'])
def login():
    pass


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    pass


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    pass


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    pass
