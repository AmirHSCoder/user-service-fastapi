from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app import crud, models
from app.api.v1 import schemas
from app.api import deps

router = APIRouter()


@router.get("/me", response_model=schemas.Profile)
async def read_profile_me(current_user: models.User = Depends(deps.get_current_user), db: AsyncSession = Depends(deps.get_db)):
    profile = await crud.profile.get_by_user_id(db, user_id=current_user.id)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile


@router.put("/me", response_model=schemas.Profile)
async def update_profile_me(
    *,
    current_user: models.User = Depends(deps.get_current_user),
    profile_in: schemas.ProfileUpdate,
    db: AsyncSession = Depends(deps.get_db),
):
    profile = await crud.profile.get_by_user_id(db, user_id=current_user.id)
    if not profile:
        profile = await crud.profile.create(db, user_id=current_user.id, obj_in=schemas.ProfileCreate(**profile_in.model_dump()))
        return profile
    profile = await crud.profile.update(db, db_obj=profile, obj_in=profile_in)
    return profile
