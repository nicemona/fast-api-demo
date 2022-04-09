from fastapi import status
from fastapi.testclient import TestClient
from requests.models import Response


def test_index(client: TestClient) -> None:
    resp: Response = client.get("/")
    assert resp.status_code == status.HTTP_200_OK
    assert resp.json() == {"message": "This is FastAPI!"}
