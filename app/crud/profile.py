from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import Optional

from app.models.profile import Profile
from app.api.v1.schemas.profile import ProfileCreate, ProfileUpdate


class CRUDProfile:
    async def get_by_user_id(self, db: AsyncSession, *, user_id: int) -> Optional[Profile]:
        result = await db.execute(select(Profile).filter(Profile.user_id == user_id))
        return result.scalars().first()

    async def create(self, db: AsyncSession, *, user_id: int, obj_in: ProfileCreate) -> Profile:
        db_obj = Profile(user_id=user_id, **obj_in.model_dump())
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def update(self, db: AsyncSession, *, db_obj: Profile, obj_in: ProfileUpdate) -> Profile:
        update_data = obj_in.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_obj, field, value)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj


profile = CRUDProfile()
