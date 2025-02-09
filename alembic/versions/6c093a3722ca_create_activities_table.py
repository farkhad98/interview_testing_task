"""create activities table

Revision ID: 6c093a3722ca
Revises: c67a2b149831
Create Date: 2025-02-08 20:51:28.747768

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6c093a3722ca'
down_revision: Union[str, None] = 'c67a2b149831'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'activities',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column(
            'parent_id',
            sa.ForeignKey('activities.id', ondelete='CASCADE'),
            nullable=True,
        ),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column(
            'updated_at',
            sa.DateTime,
            nullable=False,
        ),
    )


def downgrade() -> None:
    pass
