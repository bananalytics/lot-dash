"""updated

Revision ID: 52699334100b
Revises: 5d6af49830b8
Create Date: 2018-08-17 21:41:25.431294

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52699334100b'
down_revision = '5d6af49830b8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'user', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    # ### end Alembic commands ###
