pytest_plugins = ["pytest_asyncio"]
import os
import sys
import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app.main import app
from app.db.base import Base
from app.api import deps


@pytest.fixture(scope="session")
def db_engine():
    test_engine = create_async_engine("sqlite+aiosqlite:///:memory:", echo=False)
    async def init_models():
        async with test_engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
    import asyncio
    asyncio.get_event_loop().run_until_complete(init_models())
    yield test_engine
    asyncio.get_event_loop().run_until_complete(test_engine.dispose())


@pytest.fixture(scope="function")
def db_session(db_engine):
    async_session = sessionmaker(db_engine, class_=AsyncSession, expire_on_commit=False)
    async def get_session():
        async with async_session() as session:
            yield session
    return get_session


@pytest.fixture(scope="function")
def client(db_session):
    app.dependency_overrides[deps.get_db] = db_session
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()
