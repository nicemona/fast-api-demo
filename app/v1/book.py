from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud
from app.models.book import Book as BookModel
from utils.get_db import get_db

from .schemas import Book, BookCreate

router: APIRouter = APIRouter()


@router.post("/books", response_model=Book)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book.dict())


@router.get("/books", response_model=List[Book])
def get_book_list(
    db: Session = Depends(get_db),
    offset: int = 0,
    limit: int = 100,
):
    return crud.get_books(db, offset, limit)


@router.get("/books/{book_id}", response_model=Book)
def get_book_by_id(book_id: int, db: Session = Depends(get_db)):
    book_model = crud.get_book(db, book_id)
    if book_model is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )
    return book_model


@router.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book: Book, db: Session = Depends(get_db)):
    book_model: BookModel = crud.get_book(db, book_id)
    if book_model is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )
    book_model.title = book.title
    book_model.author = book.author
    book_model.pages = book.pages
    crud.update_book(db, book_model)
    return book_model


@router.delete("/books/{book_id}", response_model=Book)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book_model = crud.get_book(db, book_id)
    if book_model is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )
    crud.delete_book(db, book_id)
    return {"status": status.HTTP_200_OK, "transaction": "successful"}
