from flask import current_app, flash, redirect, url_for
from flask_login import login_required, current_user

from app import db
from app.models.gift import Gift
from . import web


@web.route('/my/gifts')
@login_required
def my_gifts():
    uid = current_user.id
    gifts_of_mine = Gift.get_user_gifts(uid)
    # 从查询出的我的礼物中取出书籍的isbn编号存放到集合中
    # 列表推导式
    isbn_list = [gift.isbn for gift in gifts_of_mine]
    print(isbn_list)
    count_list = Gift.get_wish_count(isbn_list)
    print(count_list)

    return 'My Gifts'


# 赠送书籍
@web.route('/gifts/book/<isbn>')
@login_required
def give_to_gifts(isbn):
    # current_user为从cookie中获取的已登录的用户信息由login_manager对象管理，current对象的实例化通过User模型下的get_user方法创建
    if current_user.can_save_to_list(isbn):
        # 使用上下文管理器来自动完成commit和回滚操作
        with db.auto_commit():
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            # 这里是增加事务处理的，如果出错后不执行回滚，则之后无法再执行插入操作
            db.session.add(gift)
    else:
        flash('这本书已添加至你的赠送清单或已存于你的心愿清单，请不要重复添加')
    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass
