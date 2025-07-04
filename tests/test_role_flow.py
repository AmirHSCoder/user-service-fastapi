import asyncio

from app import crud
from app.api.v1 import schemas
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker


def test_role_management(client, db_engine):
    user_data = {"email": "admin@example.com", "password": "secret", "full_name": "Admin"}
    resp = client.post("/api/v1/users/", json=user_data)
    assert resp.status_code == 201
    async_session = sessionmaker(db_engine, class_=AsyncSession, expire_on_commit=False)

    async def setup_role():
        async with async_session() as session:
            role = await crud.role.create(session, obj_in=schemas.RoleCreate(name="admin"))
            user = await crud.user.get_by_email(session, email=user_data["email"])
            await crud.user.add_role(session, user=user, role=role)
    asyncio.get_event_loop().run_until_complete(setup_role())

    resp = client.post(
        "/api/v1/auth/login",
        data={"username": user_data["email"], "password": user_data["password"]},
    )
    token = schemas.Token(**resp.json())

    headers = {"Authorization": f"Bearer {token.access_token}"}
    resp = client.post("/api/v1/roles/", json={"name": "manager"}, headers=headers)
    assert resp.status_code == 200
    role = schemas.Role(**resp.json())
    assert role.name == "manager"

