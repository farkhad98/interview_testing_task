from pydantic import BaseModel
from app.serializers.buildings.get_building_serializer import (
    GetBuildingSerializer
)
from app.serializers.activities.get_activity_serializer import (
    GetActivitySerializer,
)
from datetime import datetime
from typing import List


class GetOrganizationSerializer(BaseModel):
    id: int
    name: str
    phone: str
    updated_at: datetime
    created_at: datetime
    building: GetBuildingSerializer | None = None
    activities: List[GetActivitySerializer] | None = None
