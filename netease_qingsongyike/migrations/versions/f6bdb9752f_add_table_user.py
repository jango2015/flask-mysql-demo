"""'add_table_user'

Revision ID: f6bdb9752f
Revises: 4b0a107afd4
Create Date: 2016-07-28 11:35:43.053616

"""

# revision identifiers, used by Alembic.
revision = 'f6bdb9752f'
down_revision = '4b0a107afd4'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.Column('mobile', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Users')
    ### end Alembic commands ###