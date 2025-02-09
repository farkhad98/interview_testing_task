"""create organizations table

Revision ID: 14c7b1b7205d
Revises: 6c093a3722ca
Create Date: 2025-02-08 20:51:33.172550

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '14c7b1b7205d'
down_revision: Union[str, None] = '6c093a3722ca'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'organizations',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('phone', sa.String, nullable=False),
        sa.Column(
            'building_id',
            sa.Integer,
            sa.ForeignKey('buildings.id', ondelete='CASCADE'),
            nullable=False,
        ),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('updated_at', sa.DateTime, nullable=False),
    )


def downgrade() -> None:
    pass
