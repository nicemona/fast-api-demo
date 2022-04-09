from fastapi.testclient import TestClient
from pytest import fixture
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from app.models.base import BaseModel
from utils import database


@fixture(scope="session", autouse=True)
def override_db():
    database.SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
    database.CONNECTION_ARGS = {"check_same_thread": False}
    yield


@fixture()
def db_session():
    engine = create_engine(
        "sqlite:///./test.db", connect_args={"check_same_thread": False}
    )
    session = scoped_session(
        sessionmaker(
            bind=engine,
            autocommit=True,
            autoflush=True,
        )
    )
    BaseModel.metadata.create_all(bind=engine)
    yield session
    session.close()


@fixture()
def client():
    from app.main import app

    yield TestClient(app)
