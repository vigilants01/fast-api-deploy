"""add user table

Revision ID: 266d6b58df7a
Revises: 2193af19270b
Create Date: 2025-07-01 10:41:32.934783

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '266d6b58df7a'
down_revision: Union[str, Sequence[str], None] = '2193af19270b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('users',
            sa.Column('id', sa.Integer(), nullable=False),
            sa.Column('email', sa.String(), nullable=False),
            sa.Column('password', sa.String(), nullable=False),
            sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                server_default=sa.text('now()'), nullable=False),
            sa.PrimaryKeyConstraint('id'),
            sa.UniqueConstraint('email')
            )
    pass


def downgrade():
    op.drop_table('users')
    pass
