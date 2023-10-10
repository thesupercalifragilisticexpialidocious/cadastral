from datetime import datetime

from pydantic import BaseModel, Extra, Field


class InquiryCreate(BaseModel):
    latitude: float = Field(None, ge=-90, le=90)
    longitude: float = Field(None, ge=-180, le=180)
    number: str = Field(None, max_length=32)

    class Config:
        extra = Extra.forbid


class InquiryDB(InquiryCreate):
    id: int
    result: str
    date: datetime

    class Config:
        orm_mode = True
