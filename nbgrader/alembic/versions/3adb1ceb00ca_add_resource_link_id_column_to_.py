"""Add 'resource_link_id' column to assignment table

Revision ID: 3adb1ceb00ca
Revises: e43177bfe90b
Create Date: 2020-07-28 12:19:07.168363

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3adb1ceb00ca'
down_revision = 'e43177bfe90b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('assignment', sa.Column('lms_resource_link_id', sa.String(128), nullable=True))


def downgrade():
    op.drop_column('assignment', 'lms_resource_link_id')
