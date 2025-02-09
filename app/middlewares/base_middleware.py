from app.services.authorization_service import Authorization


async def authorization(access_token: str) -> dict | bool:
    return await Authorization.get_payload_from_token(access_token)
