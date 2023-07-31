"""add last few columns to posts table

Revision ID: 7635ed76865e
Revises: d157f12bdf08
Create Date: 2023-07-31 15:00:36.731314

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7635ed76865e'
down_revision = 'd157f12bdf08'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('published',sa.Boolean(),nullable=False,server_default='TRUE'))
    op.add_column('posts',sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('now()')))
    pass


def downgrade() -> None:
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass
