"""empty message

Revision ID: 5071b4e36794
Revises: 7dff6a8ad3bc
Create Date: 2021-12-13 09:50:25.732380

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5071b4e36794'
down_revision = '7dff6a8ad3bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('t_users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('age', sa.SmallInteger(), nullable=True),
    sa.Column('gender', sa.Enum('woman', 'man'), nullable=True),
    sa.Column('addr', sa.String(length=256), nullable=True),
    sa.Column('mobile', sa.Integer(), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('t_users')
    # ### end Alembic commands ###
