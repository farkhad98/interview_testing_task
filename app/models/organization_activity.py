from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from app.core.base_meta import Base
from app.models.mixins.timestamp_mixin import TimestampMixin
# from app.models.activity import Activity


class OrganizationActivity(Base, TimestampMixin):
    """
    Pivot model for organizations -> activities
    """
    __tablename__ = 'organizations_activities'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    organization_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey('organizations.id', ondelete='CASCADE'),
        index=True
    )
    organization = relationship(
        'Organization',
        back_populates='pivot_activities',
    )
    activity_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey('activities.id', ondelete='CASCADE'),
        index=True
    )
    activity = relationship('Activity', back_populates='pivot_organizations')
