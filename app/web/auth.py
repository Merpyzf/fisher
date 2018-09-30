from flask import render_template

from . import web

__author__ = '七月'


@web.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('auth/register.html',form={'data':{}})

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
