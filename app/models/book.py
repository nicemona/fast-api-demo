from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String

from app.models.base import BaseModel


class Book(BaseModel):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    author = Column(String)
    pages = Column(Integer)
