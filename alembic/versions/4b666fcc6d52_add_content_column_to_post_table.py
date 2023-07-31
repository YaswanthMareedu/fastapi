"""add content column to post table

Revision ID: 4b666fcc6d52
Revises: ad4aba12b4c6
Create Date: 2023-07-31 13:48:28.404388

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b666fcc6d52'
down_revision = 'ad4aba12b4c6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
