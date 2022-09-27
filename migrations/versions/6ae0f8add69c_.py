"""empty message

Revision ID: 6ae0f8add69c
Revises: 2d0ec186bc0e
Create Date: 2022-09-27 21:40:32.997238

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ae0f8add69c'
down_revision = '2d0ec186bc0e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('e2U',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_enterprise', sa.Integer(), nullable=True),
    sa.Column('id_user', sa.Integer(), nullable=True),
    sa.Column('level', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('e2U')
    # ### end Alembic commands ###
