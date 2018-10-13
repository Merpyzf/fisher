"""empty message

Revision ID: e96a32dad58d
Revises: e274098fdc01
Create Date: 2018-10-08 22:07:14.824895

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e96a32dad58d'
down_revision = 'e274098fdc01'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('book', 'create_time')
    op.drop_column('gift', 'create_time')
    op.drop_column('user', 'create_time')
    op.drop_column('wish', 'create_time')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('wish', sa.Column('create_time', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('create_time', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.add_column('gift', sa.Column('create_time', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.add_column('book', sa.Column('create_time', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    # ### end Alembic commands ###