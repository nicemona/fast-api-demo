from fastapi import APIRouter
from pydantic import BaseModel, Field

router: APIRouter = APIRouter()


class BookBase(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    pages: int = Field(gt=-1, lt=100000)


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int

    class Config:
        orm_mode = True
