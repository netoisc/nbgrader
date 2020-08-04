"""Add lms_lineitems_endpoint' column to course

Revision ID: 2f06e9462d32
Revises: e43177bfe90b
Create Date: 2020-07-31 16:11:22.134115

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f06e9462d32'
down_revision = 'e43177bfe90b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('course', sa.Column('lms_lineitems_endpoint', sa.String(128), nullable=True))


def downgrade():
    op.drop_column('course', 'lms_lineitems_endpoint')
