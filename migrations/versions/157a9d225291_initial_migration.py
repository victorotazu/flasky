"""initial migration

Revision ID: 157a9d225291
Revises: 
Create Date: 2019-01-08 11:59:00.979485

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '157a9d225291'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('name', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'name')
    # ### end Alembic commands ###
