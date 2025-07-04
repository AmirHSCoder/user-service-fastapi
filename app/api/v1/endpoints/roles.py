from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app import crud, models
from app.api.v1 import schemas
from app.api import deps

router = APIRouter()


@router.post("/", response_model=schemas.Role)
async def create_role(
    *,
    db: AsyncSession = Depends(deps.get_db),
    current_user: models.User = Depends(deps.require_role("admin")),
    role_in: schemas.RoleCreate,
):
    existing = await crud.role.get_by_name(db, name=role_in.name)
    if existing:
        raise HTTPException(status_code=400, detail="Role already exists")
    return await crud.role.create(db, obj_in=role_in)


@router.post("/assign/{user_id}/{role_name}", status_code=status.HTTP_200_OK)
async def assign_role(
    user_id: int,
    role_name: str,
    db: AsyncSession = Depends(deps.get_db),
    current_user: models.User = Depends(deps.require_role("admin")),
):
    user = await crud.user.get(db, id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    role = await crud.role.get_by_name(db, name=role_name)
    if not role:
        role = await crud.role.create(db, obj_in=schemas.RoleCreate(name=role_name))
    await crud.user.add_role(db, user=user, role=role)
    return {"detail": "role assigned"}


@router.get("/me", response_model=list[schemas.Role])
async def read_my_roles(
    current_user: models.User = Depends(deps.get_current_user),
):
    return current_user.roles
