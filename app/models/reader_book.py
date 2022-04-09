from sqlalchemy.orm import relationship
from sqlalchemy.orm.relationships import RelationshipProperty
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer

from app.models.base import BaseModel


class ReaderBook(BaseModel):
    __tablename__ = "readers_books"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    reader_id = Column(Integer, ForeignKey("readers.id"), nullable=False)

    book: RelationshipProperty = relationship("Book", uselist=False)
    reader: RelationshipProperty = relationship("Reader", uselist=False)
