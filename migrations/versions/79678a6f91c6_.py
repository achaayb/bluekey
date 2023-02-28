"""empty message

Revision ID: 79678a6f91c6
Revises: 52eb5dfacd72
Create Date: 2023-02-28 02:35:09.741652

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79678a6f91c6'
down_revision = '52eb5dfacd72'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('crypters', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('crypters', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###
