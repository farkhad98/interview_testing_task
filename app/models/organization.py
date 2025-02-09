from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from app.core.base_meta import Base
from app.models.mixins.timestamp_mixin import TimestampMixin
from app.models.building import Building
from app.models.organization_activity import OrganizationActivity


class Organization(Base, TimestampMixin):
    __tablename__ = 'organizations'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    phone: Mapped[str] = mapped_column(String(20), nullable=False)
    building_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey('buildings.id', ondelete='CASCADE'), nullable=False
    )

    building = relationship(Building, back_populates='organizations')
    pivot_activities = relationship(
        OrganizationActivity,
        back_populates='organization',
    )
