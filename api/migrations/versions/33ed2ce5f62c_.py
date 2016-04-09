"""empty message

Revision ID: 33ed2ce5f62c
Revises: 4ceebc947f4e
Create Date: 2016-04-09 12:53:40.026887

"""

# revision identifiers, used by Alembic.
revision = '33ed2ce5f62c'
down_revision = '4ceebc947f4e'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('site',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('public_key', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('site')
    ### end Alembic commands ###