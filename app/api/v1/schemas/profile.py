from pydantic import BaseModel
from typing import Optional


class ProfileBase(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None


class ProfileCreate(ProfileBase):
    pass


class ProfileUpdate(ProfileBase):
    pass


class Profile(ProfileBase):
    id: int

    class Config:
        orm_mode = True
