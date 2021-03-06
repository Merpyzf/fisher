from flask import render_template, request, url_for, flash
from werkzeug.security import generate_password_hash

from app import db
from app.models.user import User
from app.forms.auth import RegisterForm, LoginForm
from flask import redirect
from flask_login import login_user
from . import web

@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    # 验证用户提交的表单数据
    if request.method == 'POST' and form.validate():
        with db.auto_commit():
            user = User()
            # form.data获取客户端提交的字典类型的参数
            user.set_attrs(form.data)
            # 将数据存储到数据库中
            db.session.add(user)
        return redirect(url_for('web.login'))
    # form.errors 以字典的形式存放表单的验证信息
    # print(form.errors)
    return render_template('auth/register.html',form=form)

@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        # 如果用户登录的表单数据格式校验通过，则根据用户提交的邮箱地址查询用户信息
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=True)
            next = request.args.get('next')
            # 默认的next后边跟的视图的地址时以/开头的，增加一些判断为了避免重定向攻击
            if not next or not next.startswith('/'):
                # 如果不存在next参数值或者next后面的参数值被手动修改了则强制跳转到应用的首页
                next = url_for('web.index')
            return redirect(next)
        else:
            flash('账号不存在或密码错误')
    return render_template('auth/login.html', form=form)


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
