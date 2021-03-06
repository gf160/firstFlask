"""empty message

Revision ID: 0df37c969889
Revises: 05cda2a3daee
Create Date: 2021-08-15 18:06:03.379690

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0df37c969889'
down_revision = '05cda2a3daee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uq_user_user_email'), ['email'])
        batch_op.create_unique_constraint(batch_op.f('uq_user_user_user_id'), ['user_id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_user_user_user_id'), type_='unique')
        batch_op.drop_constraint(batch_op.f('uq_user_user_email'), type_='unique')

    # ### end Alembic commands ###
