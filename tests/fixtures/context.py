import pytest
from app.run import app


@pytest.fixture
def client():
    with app.app_context():
        with app.test_client() as client:
            yield client
