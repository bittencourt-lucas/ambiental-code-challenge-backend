from datetime import datetime
from httpx import Response
import pytest
from app.jobs.fetch_forecast_job import FetchForecastJob

CURRENT_TIMESTAMP = datetime.now()


class MockResponse:
    def __init__(self):
        self.status_code = 200

    @staticmethod
    def json() -> dict:
        return {"mock_info": "mock"}


@pytest.fixture(name="_mock_response")
def fixture_mock_response(monkeypatch):
    def mock_execute() -> tuple:
        return (MockResponse(), CURRENT_TIMESTAMP)

    monkeypatch.setattr(FetchForecastJob, "execute", mock_execute)


def test_fetch_forecast_job(_mock_response):
    data: dict = {"mock_info": "mock"}
    status_code: int = 200

    response: Response
    timestamp: datetime
    response, timestamp = FetchForecastJob.execute()

    assert response.json() == data
    assert response.status_code == status_code
    assert timestamp == CURRENT_TIMESTAMP
