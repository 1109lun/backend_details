from pydantic import BaseModel , Field
from datetime import date, datetime
from typing import Optional

class UserCreate(BaseModel):
    username: str
    password: str
    birthday: date

class UserOut(BaseModel):
    username: str
    birthday: Optional[date]
    create_time: Optional[datetime]
    last_login: Optional[datetime]

    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    password: Optional[str] = Field(default=None)
    birthday: Optional[date] = Field(default=None)
