"""Test server."""

from http import HTTPStatus

from fastapi.testclient import TestClient
from zipalyzer import __version__
from zipalyzer.server import app

client = TestClient(app)


def test_read_main() -> None:
    """Test getting the root route."""
    response = client.get("/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "version": __version__,
        "server_commit": "development",
    }
