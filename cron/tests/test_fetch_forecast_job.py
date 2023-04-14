import pytest
from app.jobs.fetch_forecast_job import FetchForecastJob


class MockResponse:
    def __init__(self):
        self.status_code = 200

    @staticmethod
    def json() -> dict:
        return {"mock_info": "mock"}


@pytest.fixture
def mock_response(monkeypatch):
    def mock_execute(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(FetchForecastJob, "execute", mock_execute)


def test_fetch_forecast_job(mock_response):
    data: dict = {"mock_info": "mock"}
    status_code: int = 200

    result = FetchForecastJob.execute()

    assert result.json() == data
    assert result.status_code == status_code
