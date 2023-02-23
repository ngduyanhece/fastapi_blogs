"""add vote table

Revision ID: 410cfcc35fea
Revises: cd20bb44ba3f
Create Date: 2023-02-22 20:49:33.451878

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '410cfcc35fea'
down_revision = 'cd20bb44ba3f'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('votes',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'post_id')
    )
    pass


def downgrade():
    op.drop_table('votes')
    pass
