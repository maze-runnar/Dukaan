"""empty message

Revision ID: 5943d6c8cfc6
Revises: 2a733285c73e
Create Date: 2021-12-29 08:51:30.278045

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5943d6c8cfc6'
down_revision = '2a733285c73e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('khata', sa.Column('payer_name', sa.String()))
    #op.execute("UPDATE khata SET \"payer_name\" = \'other\' WHERE TRUE")
    # pass


def downgrade():
    op.drop_column('khata', 'payer_name')
    # pass
