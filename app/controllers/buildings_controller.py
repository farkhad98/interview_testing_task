from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List
from app.core.base_meta import get_async_db
from app.models.building import Building
from app.serializers.organizations.get_organization_serializer import (
    GetBuildingSerializer,
)
from app.middlewares.base_middleware import authorization


router = APIRouter(
    prefix='/buildings',
    tags=['buildings'],
    responses={status.HTTP_404_NOT_FOUND: {'description': 'Not found'}},
)


@router.get('/', response_model=List[GetBuildingSerializer])
async def buildings(
    _: str = Depends(authorization),
    db: AsyncSession = Depends(get_async_db),
    page: int = 1,
    page_size: int = 10,
):

    buildings_query = await db.execute(
        select(Building).limit(page_size).offset((page - 1) * page_size)
    )
    buildings = buildings_query.scalars().all()
    return buildings
