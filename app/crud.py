from typing import Dict

from sqlalchemy.orm import Session

from app.models.book import Book as BookModel


def get_book(db: Session, book_id: int):
    return db.query(BookModel).filter(BookModel.id == book_id).first()


def get_books(db: Session, offset: int = 0, limit: int = 100):
    return db.query(BookModel).offset(offset).limit(limit).all()


def create_book(db: Session, book: Dict):
    db_book = BookModel(**book)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def update_book(db: Session, book_model: BookModel):
    db.add(book_model)
    db.commit()


def delete_book(db: Session, book_id: int):
    db.query(BookModel).filter(BookModel.id == book_id).delete()
    db.commit()
