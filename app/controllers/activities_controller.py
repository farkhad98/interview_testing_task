from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
import json
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from typing import List
from app.core.base_meta import get_async_db
from app.models.activity import Activity
from app.serializers.activities.get_activity_serializer import (
    GetActivitySerializer
)
from app.middlewares.base_middleware import authorization
from sqlalchemy import asc
from app.core.base_meta import get_async_redis


router = APIRouter(
    prefix='/activities',
    tags=['activities'],
    responses={status.HTTP_404_NOT_FOUND: {'description': 'Not found'}},
)


@router.get('/', response_model=List[GetActivitySerializer])
async def activities(
    pk: int | None = None,
    _: str = Depends(authorization),
    db: AsyncSession = Depends(get_async_db),
    page: int = 1,
    page_size: int = 10,
    redis: AsyncSession = Depends(get_async_redis),
):
    cache_key = f'activities:{pk},{page}:{page_size}'
    cached_activities = await redis.get(cache_key)
    if cached_activities:
        print('redis returned')
        return json.loads(cached_activities)
    where_claus = []
    if pk is not None:
        where_claus.append(
            Activity.id == pk
        )
    activities_query = await db.execute(
        select(Activity)
        .options(
            selectinload(Activity.children),
            selectinload(Activity.children).selectinload(Activity.children)
        )
        .where(*where_claus)
        .limit(page_size)
        .offset((page - 1) * page_size)
        .order_by(asc(Activity.id))
    )
    activities = activities_query.unique().scalars().all()
    if activities:
        serialized_activities = [
            GetActivitySerializer(
                id=activity.id,
                name=activity.name,
                parent_id=activity.parent_id,
                children=[
                    GetActivitySerializer(
                        id=child.id,
                        name=child.name,
                        parent_id=child.parent_id,
                        children=[
                            GetActivitySerializer(
                                id=sub_child.id,
                                name=sub_child.name,
                                parent_id=sub_child.parent_id,
                                updated_at=sub_child.updated_at,
                                created_at=sub_child.created_at,
                            )
                            for sub_child in child.children
                        ],
                        updated_at=child.updated_at,
                        created_at=child.created_at,
                    )
                    for child in activity.children
                ],
                updated_at=activity.updated_at,
                created_at=activity.created_at,
            ).model_dump(mode='json')
            for activity in activities
        ]
        await redis.set(cache_key, json.dumps(serialized_activities))
        await redis.expire(cache_key, 86400)
    return serialized_activities
