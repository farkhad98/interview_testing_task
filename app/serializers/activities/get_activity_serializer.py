from pydantic import BaseModel
from datetime import datetime
from typing import List


class GetActivitySerializer(BaseModel):
    id: int
    name: str
    parent_id: int | None = None
    children: List['GetActivitySerializer'] | None = None
    updated_at: datetime
    created_at: datetime
