import jwt
import datetime
from fastapi import HTTPException
from app.configs.environments import env
from starlette import status


class Authorization:
    @staticmethod
    async def create_access_token() -> str:
        payload: dict = {
            'exp': datetime.datetime.now(
                tz=datetime.timezone.utc,
            ) + datetime.timedelta(hours=2),
        }
        return jwt.encode(payload, env.secret_key, algorithm=env.algorithm)

    @staticmethod
    async def get_payload_from_token(token: str) -> dict:
        # token: str = token.split(' ')[1]

        try:
            return jwt.decode(
                token,
                env.secret_key,
                algorithms=[env.algorithm],
            )
        except jwt.exceptions.ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Token is expired',
            )
        except jwt.exceptions.DecodeError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Incorrect token type',
            )
