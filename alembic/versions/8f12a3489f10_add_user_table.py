"""add user table

Revision ID: 8f12a3489f10
Revises: 4b666fcc6d52
Create Date: 2023-07-31 13:58:37.752559

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f12a3489f10'
down_revision = '4b666fcc6d52'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',sa.Column('id',sa.Integer(),nullable=False),
                    sa.Column('email',sa.String(),nullable=False),
                    sa.Column('password',sa.String(),nullable=False),
                    sa.Column('created_at',sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'),nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))
    pass
    


def downgrade() -> None:
    op.drop_table('users')
    pass
