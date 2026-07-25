import os

os.environ["ENV"] = "test"
from app.core.database import engine

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.core.database import SessionLocal
from app.core.database import get_db


@pytest.fixture
def user():
    return {
        "name": "francisco"
    }

@pytest.fixture
def client(db_session):
    
    def override_get_db():
        yield db_session
        
    app.dependency_overrides[get_db] = override_get_db
    
    with TestClient( app ) as client:
        yield client
        
    app.dependency_overrides.clear()

@pytest.fixture
def db_session():

    connection = engine.connect()

    transaction = connection.begin()

    session = SessionLocal(bind=connection)

    try:
        yield session

    finally:
        session.close()
        transaction.rollback()
        connection.close()