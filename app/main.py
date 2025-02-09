from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends
from redis.asyncio import Redis
from sqlalchemy.ext.asyncio import AsyncSession
from app.controllers import authorization_controller
from app.controllers import buildings_controller
from app.controllers import activities_controller
from app.controllers import organizations_controller
from app.core.base_meta import get_async_db
from app.core.base_meta import get_async_redis
from app.configs.environments import env
from app.fakers.initial_seed import create_initial_state


app = FastAPI()
# Router
app.include_router(authorization_controller.router, prefix='/api/v1')
app.include_router(buildings_controller.router, prefix='/api/v1')
app.include_router(activities_controller.router, prefix='/api/v1')
app.include_router(organizations_controller.router, prefix='/api/v1')


origins = env.cors_allowed_origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/')
async def root(
    db: AsyncSession = Depends(get_async_db),
    redis: Redis = Depends(get_async_redis),
) -> dict:
    await redis.set('status', 'OK')
    await redis.expire('status', 300)
    await create_initial_state(db)
    return {
        'redis': {
            'status': await redis.get('status'),
            'default_ttl': str(await redis.ttl('status')) + ' seconds',
        },
    }
