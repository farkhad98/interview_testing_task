from pydantic import BaseModel


class GetStaticTokenSerializer(BaseModel):
    static_token: str
