"""add foreign key to post table

Revision ID: fef5561b764c
Revises: ea97d0a2d8a8
Create Date: 2023-02-22 20:00:01.315962

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fef5561b764c'
down_revision = 'ea97d0a2d8a8'
branch_labels = None
depends_on = None


def upgrade():
    # add foreign key to posts table
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=[
                          'owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
