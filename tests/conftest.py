import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

# ... setup test database and client

def override_get_db():
    # ... return a test database session
    pass

app.dependency_overrides[deps.get_db] = override_get_db
