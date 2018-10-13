from flask import flash, redirect, url_for
from flask_login import current_user, login_required

from app import db, Gift, Wish
from app.web.auth import login
from . import web



@web.route('/my/wish')
def my_wish():
    pass


# 加入心愿清单功能
@web.route('/wish/book/<isbn>')
@login_required
def save_to_wish(isbn):
    # current_user为从cookie中获取的已登录的用户信息由login_manager对象管理，current对象的实例化通过User模型下的get_user方法创建
    if current_user.can_save_to_list(isbn):
        # 使用上下文管理器来自动完成commit和回滚操作
        with db.auto_commit():
            wish = Wish()
            wish.isbn = isbn
            wish.uid = current_user.id
            # 这里是增加事务处理的，如果出错后不执行回滚，则之后无法再执行插入操作
            db.session.add(wish)
    else:
        flash('这本书已添加至你的赠送清单或已存于你的心愿清单，请不要重复添加')
    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/satisfy/wish/<int:wid>')
def satisfy_wish(wid):
    pass


@web.route('/wish/book/<isbn>/redraw')
def redraw_from_wish(isbn):
    pass
