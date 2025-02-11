from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from app.core.base_meta import Base

from app.models.mixins.timestamp_mixin import TimestampMixin
from app.models.organization_activity import OrganizationActivity


class Activity(Base, TimestampMixin):
    __tablename__ = 'activities'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    parent_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("activities.id", ondelete="SET NULL"),
        nullable=True,
    )
    parent = relationship(
        "Activity",
        remote_side=[id],
        back_populates="children",
    )
    children = relationship(
        "Activity",
        back_populates="parent",
        lazy="selectin",
        cascade="all, delete-orphan",
    )
    pivot_organizations = relationship(
        OrganizationActivity,
        back_populates="activity",
    )
