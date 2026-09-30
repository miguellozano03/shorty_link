from datetime import datetime
from pydantic import BaseModel, ConfigDict, computed_field, HttpUrl
from shortener.utils import build_short_url

class UrlCreateSchema(BaseModel):
    title: str
    long_url: HttpUrl

class UrlSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str | None
    long_url: str
    code: str
    created_at: datetime

    @computed_field
    @property
    def short_url(self) -> str:
        return build_short_url(self.code)

class UrlUpdateSchema(BaseModel):
    title: str | None = None
    long_url: str | None = None