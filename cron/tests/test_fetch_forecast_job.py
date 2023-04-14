import pytest
from httpx import Response
from datetime import datetime
from app.jobs.fetch_forecast_job import FetchForecastJob

CURRENT_TIMESTAMP = datetime.now()

class MockResponse:
    def __init__(self):
        self.status_code = 200

    @staticmethod
    def json() -> dict:
        return {"mock_info": "mock"}


@pytest.fixture
def mock_response(monkeypatch):
    def mock_execute(*args, **kwargs) -> tuple:
        return (MockResponse(), CURRENT_TIMESTAMP)

    monkeypatch.setattr(FetchForecastJob, "execute", mock_execute)


def test_fetch_forecast_job(mock_response):
    data: dict = {"mock_info": "mock"}
    status_code: int = 200

    response: Response
    timestamp: datetime
    response, timestamp = FetchForecastJob.execute()

    assert response.json() == data
    assert response.status_code == status_code
    assert timestamp == CURRENT_TIMESTAMP
