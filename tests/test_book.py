from fastapi import status
from fastapi.testclient import TestClient
from requests.models import Response
from sqlalchemy.orm import Session

from app.models.book import Book


def test_create_book(client: TestClient, db_session: Session):
    book = {
        "title": "Spiderman",
        "author": "David C.",
        "pages": 232,
    }
    response: Response = client.post(
        "/v1/books",
        json=book,
    )
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["title"] == book["title"]
    assert data["author"] == book["author"]
    assert "id" in data
    book_id = data["id"]

    response = client.get(f"/v1/books/{book_id}")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["title"] == book["title"]
    assert data["author"] == book["author"]
    assert data["id"] == book_id

    db_session.query(Book).delete()
