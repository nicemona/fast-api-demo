from typing import Dict

from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = (
    "postgresql://"
    f"{config('DB_USER')}:{config('DB_PASSWORD')}"
    "@localhost:5432/book_store"
)
CONNECTION_ARGS: Dict = {}


def create_session():
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)
