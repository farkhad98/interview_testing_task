from sqlalchemy import Numeric
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from app.core.base_meta import Base
from app.models.mixins.timestamp_mixin import TimestampMixin
# from app.models.organization import Organization


class Building(Base, TimestampMixin):
    __tablename__ = 'buildings'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    address: Mapped[str] = mapped_column(String(128), nullable=False)
    longitude: Mapped[float] = mapped_column(Numeric, nullable=False)
    latitude: Mapped[float] = mapped_column(Numeric, nullable=False)
    organizations = relationship('Organization', back_populates='building')
