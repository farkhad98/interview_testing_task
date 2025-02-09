from redis.asyncio import Redis
from app.configs.environments import env
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase


SQLALCHEMY_ASYNC_DATABASE_URL = env.db_async_url

async_engine = create_async_engine(SQLALCHEMY_ASYNC_DATABASE_URL, echo=True)


class Base(DeclarativeBase):
    pass


AsyncSessionLocal = async_sessionmaker(async_engine, expire_on_commit=False)


async def get_async_db() -> AsyncSession:
    async with AsyncSessionLocal() as async_db:
        try:
            yield async_db
        finally:
            await async_db.close()


async def get_async_redis():
    redis = Redis(
        host=env.redis_host,
        port=env.redis_port,
        password=env.redis_password
    )
    try:
        yield redis
    finally:
        await redis.close()
