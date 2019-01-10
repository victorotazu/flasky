"""Replaced users.name with users.full_name

Revision ID: fb6f3b04bd7e
Revises: 157a9d225291
Create Date: 2019-01-08 12:05:19.521157

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb6f3b04bd7e'
down_revision = '157a9d225291'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('full_name', sa.String(length=128), nullable=True))
    op.drop_column('users', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('name', sa.VARCHAR(length=100), nullable=True))
    op.drop_column('users', 'full_name')
    # ### end Alembic commands ###