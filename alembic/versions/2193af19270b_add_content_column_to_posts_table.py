"""add content column to posts table

Revision ID: 2193af19270b
Revises: 2a106ca51c0e
Create Date: 2025-07-01 10:30:12.674921

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2193af19270b'
down_revision: Union[str, Sequence[str], None] = '2a106ca51c0e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
