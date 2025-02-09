"""create buildings table

Revision ID: c67a2b149831
Revises: 
Create Date: 2025-02-08 20:51:21.008703

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c67a2b149831'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'buildings',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('address', sa.String, nullable=False),
        sa.Column('longitude', sa.Float, nullable=False),
        sa.Column('latitude', sa.Float, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('updated_at', sa.DateTime, nullable=False),
    )


def downgrade() -> None:
    pass
