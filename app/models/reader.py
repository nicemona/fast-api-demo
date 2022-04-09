from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String

from app.models.base import BaseModel


class Reader(BaseModel):
    __tablename__ = "readers"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, unique=True, index=True)
    last_name = Column(String)
