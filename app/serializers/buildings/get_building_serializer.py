from pydantic import BaseModel
from datetime import datetime


class GetBuildingSerializer(BaseModel):
    id: int
    address: str
    longitude: float
    latitude: float
    updated_at: datetime
    created_at: datetime
