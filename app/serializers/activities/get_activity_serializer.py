from pydantic import BaseModel
from datetime import datetime


class GetActivitySerializer(BaseModel):
    id: int
    name: str
    parent_id: int | None = None
    updated_at: datetime
    created_at: datetime
