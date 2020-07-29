"""Add 'lms_lineitem_id' column to assignment

Revision ID: 025a454cf740
Revises: 3adb1ceb00ca
Create Date: 2020-07-29 10:46:20.907380

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '025a454cf740'
down_revision = '3adb1ceb00ca'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('assignment', sa.Column('lms_lineitem_id', sa.String(128), nullable=True))


def downgrade():
    op.drop_column('assignment', 'lms_lineitem_id')
