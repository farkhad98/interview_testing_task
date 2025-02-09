from fastapi import APIRouter
from fastapi import status
from app.services.authorization_service import Authorization
from fastapi.responses import JSONResponse
from app.serializers.authorization.authorization_serializer import (
    GetStaticTokenSerializer,
)


router = APIRouter(
    prefix='/static_token',
    tags=['static_token'],
    responses={status.HTTP_404_NOT_FOUND: {'description': 'Not found'}},
)


authorization_service = Authorization()


@router.get('/', response_model=GetStaticTokenSerializer)
async def obtain_static_token():
    # TODO: add authorization on purpose
    static_token = await authorization_service.create_access_token()
    return JSONResponse(content={"static_token": static_token})
