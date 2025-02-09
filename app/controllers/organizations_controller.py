from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import and_, select
from sqlalchemy.orm import joinedload
from typing import List
from app.core.base_meta import get_async_db
from app.models.activity import Activity
from app.models.building import Building
from app.models.organization import Organization
from app.models.organization_activity import OrganizationActivity
from app.serializers.organizations.organizations_filter_serializer import (
    OrganizationsFilterSerializer,
)
from app.serializers.organizations.get_organization_serializer import (
    GetOrganizationSerializer,
    GetBuildingSerializer,
    GetActivitySerializer,
)
from app.middlewares.base_middleware import authorization


router = APIRouter(
    prefix='/organizations',
    tags=['organizations'],
    responses={status.HTTP_404_NOT_FOUND: {'description': 'Not found'}},
)


@router.get('/', response_model=List[
    GetOrganizationSerializer,
])
async def organizations_list(
    filters: OrganizationsFilterSerializer = Depends(
        OrganizationsFilterSerializer,
    ),
    db: AsyncSession = Depends(get_async_db),
    _=Depends(authorization),
):
    where_clause = []

    if all([
            filters.left_top_coordinates_x,
            filters.left_top_coordinates_y,
            filters.right_top_coordinates_x,
            filters.right_top_coordinates_y,
            filters.right_bottom_coordinates_x,
            filters.right_bottom_coordinates_y,
            filters.left_bottom_coordinates_x,
            filters.left_bottom_coordinates_y,
    ]):
        where_clause.append(
            Organization.building.has(
                and_(
                    Building.latitude <= filters.left_top_coordinates_y,
                    Building.longitude >= filters.left_top_coordinates_x,

                    Building.latitude <= filters.right_top_coordinates_y,
                    Building.longitude <= filters.right_top_coordinates_x,

                    Building.latitude >= filters.right_bottom_coordinates_y,
                    Building.longitude <= filters.right_bottom_coordinates_x,

                    Building.latitude >= filters.left_bottom_coordinates_y,
                    Building.longitude >= filters.left_bottom_coordinates_x,
                ),
            ),
        )

    if filters.building_id is not None:
        where_clause.append(
            Organization.building_id == filters.building_id,
        )

    if filters.activity_id is not None:
        activities_ids = await db.execute(
            select(Activity.id).where(
                Activity.parent_id == filters.activity_id,
                Activity.parent_id == Activity.id,
            )
        )
        activities_ids = [
            activity_id for activity_id in activities_ids.unique().scalars()
        ]
        activities_ids.append(filters.activity_id)
        where_clause.append(
            Organization.pivot_activities.any(
                OrganizationActivity.activity_id.in_(activities_ids),
            ),
        )

    if filters.name is not None:
        where_clause.append(
            Organization.name.ilike(f"%{filters.name}%")
        )

    organizations_query = select(Organization).options(
        joinedload(Organization.building),
        joinedload(Organization.pivot_activities).joinedload(
            OrganizationActivity.activity,
        ),
    ).where(
        *where_clause,
    )
    organizations = await db.execute(organizations_query)
    organizations = organizations.unique().scalars()

    return [
        GetOrganizationSerializer(
            id=organization.id,
            name=organization.name,
            phone=organization.phone,
            updated_at=organization.updated_at,
            created_at=organization.created_at,
            building=(
                GetBuildingSerializer(
                    id=organization.building.id,
                    address=organization.building.address,
                    longitude=organization.building.longitude,
                    latitude=organization.building.latitude,
                    updated_at=organization.building.updated_at,
                    created_at=organization.building.created_at,
                )
                if organization.building_id is not None else None
            ),
            activities=[
                GetActivitySerializer(
                    id=pivot_activity.activity.id,
                    name=pivot_activity.activity.name,
                    parent_id=pivot_activity.activity.parent_id,
                    updated_at=pivot_activity.activity.updated_at,
                    created_at=pivot_activity.activity.created_at,
                )
                for pivot_activity in organization.pivot_activities
            ],
        )
        for organization in organizations
    ]


@router.get('/{pk}', response_model=GetOrganizationSerializer)
async def organization_detail(
    pk: int,
    db: AsyncSession = Depends(get_async_db),
    _=Depends(authorization),
):
    organization_query = select(Organization).where(
        Organization.id == pk
    ).options(
        joinedload(Organization.building),
        joinedload(Organization.pivot_activities).joinedload(
            OrganizationActivity.activity,
        ),
    )
    organization = await db.execute(organization_query)
    organization = organization.scalars().first()
    return GetOrganizationSerializer(
            id=organization.id,
            name=organization.name,
            phone=organization.phone,
            updated_at=organization.updated_at,
            created_at=organization.created_at,
            building=(
                GetBuildingSerializer(
                    id=organization.building.id,
                    address=organization.building.address,
                    longitude=organization.building.longitude,
                    latitude=organization.building.latitude,
                    updated_at=organization.building.updated_at,
                    created_at=organization.building.created_at,
                )
                if organization.building_id is not None else None
            ),
            activities=[
                GetActivitySerializer(
                    id=pivot_activity.activity.id,
                    name=pivot_activity.activity.name,
                    parent_id=pivot_activity.activity.parent_id,
                    updated_at=pivot_activity.activity.updated_at,
                    created_at=pivot_activity.activity.created_at,
                )
                for pivot_activity in organization.pivot_activities
            ],
        )
