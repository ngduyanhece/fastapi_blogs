"""add content column to posts table

Revision ID: 134974f7f047
Revises: 63ab3aa1d972
Create Date: 2023-02-22 19:38:03.758077

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '134974f7f047'
down_revision = '63ab3aa1d972'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
