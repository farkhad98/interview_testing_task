"""create organizations activities table

Revision ID: 53302fff5abd
Revises: 14c7b1b7205d
Create Date: 2025-02-08 20:51:40.433881

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '53302fff5abd'
down_revision: Union[str, None] = '14c7b1b7205d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'organizations_activities',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column(
            'organization_id',
            sa.Integer,
            sa.ForeignKey('organizations.id', ondelete='CASCADE'),
            nullable=False,
        ),
        sa.Column(
            'activity_id',
            sa.Integer, sa.ForeignKey('activities.id', ondelete='CASCADE'),
            nullable=False,
        ),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('updated_at', sa.DateTime, nullable=False),
    )


def downgrade() -> None:
    pass
