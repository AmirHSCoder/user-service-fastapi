from typing import Optional, Sequence
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.role import Role
from app.api.v1.schemas.role import RoleCreate

class CRUDRole:
    async def get(self, db: AsyncSession, id: int) -> Optional[Role]:
        result = await db.execute(select(Role).filter(Role.id == id))
        return result.scalars().first()

    async def get_by_name(self, db: AsyncSession, *, name: str) -> Optional[Role]:
        result = await db.execute(select(Role).filter(Role.name == name))
        return result.scalars().first()

    async def get_multi(self, db: AsyncSession) -> Sequence[Role]:
        result = await db.execute(select(Role))
        return result.scalars().all()

    async def create(self, db: AsyncSession, *, obj_in: RoleCreate) -> Role:
        db_obj = Role(name=obj_in.name)
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

role = CRUDRole()
