from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
import json
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List
from app.core.base_meta import get_async_db
from app.models.activity import Activity
from app.serializers.activities.get_activity_serializer import (
    GetActivitySerializer
)
from app.middlewares.base_middleware import authorization
from app.core.base_meta import get_async_redis


router = APIRouter(
    prefix='/activities',
    tags=['activities'],
    responses={status.HTTP_404_NOT_FOUND: {'description': 'Not found'}},
)


@router.get('/', response_model=List[GetActivitySerializer], summary="")
async def activities(
    _: str = Depends(authorization),
    db: AsyncSession = Depends(get_async_db),
    page: int = 1,
    page_size: int = 10,
    redis: AsyncSession = Depends(get_async_redis),
):
    cache_key = f'activities:{page}:{page_size}'
    cached_activities = await redis.get(cache_key)
    if cached_activities:
        return json.loads(cached_activities)

    activities_query = await db.execute(
        select(Activity).limit(page_size).offset((page - 1) * page_size)
    )
    activities = activities_query.scalars().all()
    if activities:
        serialized_activities = [
            GetActivitySerializer(
                id=activity.id,
                name=activity.name,
                parent_id=activity.parent_id,
                updated_at=activity.updated_at,
                created_at=activity.created_at,
            ).model_dump(mode='json')
            for activity in activities
        ]
        await redis.set(cache_key, json.dumps(serialized_activities))
        await redis.expire(cache_key, 86400)
    return activities
