from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_async_url: str = Field(..., alias='DATABASE_ASYNC_URL')
    db_url: str = Field(..., alias='DATABASE_URL')
    secret_key: str = Field(..., alias='SECRET_KEY')
    algorithm: str = Field(..., alias='ALGORITHM')
    redis_host: str = Field(..., alias='REDIS_HOST')
    redis_port: str = Field(..., alias='REDIS_PORT')
    redis_password: str = Field(..., alias='REDIS_PASSWORD')
    cors_allowed_origins: str = Field(..., alias='CORS_ALLOWED_ORIGINS')


env: Settings = Settings()
