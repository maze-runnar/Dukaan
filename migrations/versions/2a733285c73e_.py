"""empty message

Revision ID: 2a733285c73e
Revises: 
Create Date: 2021-12-27 20:51:09.334821

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a733285c73e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('items', sa.Column('category', sa.String()))
    op.execute("UPDATE items SET \"category\" = \'other\' WHERE TRUE")


def downgrade():
    op.drop_column('items', 'category')
