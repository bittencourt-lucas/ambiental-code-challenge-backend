from datetime import datetime
from httpx import Response
from app.jobs.fetch_forecast_job import FetchForecastJob

CURRENT_TIMESTAMP = datetime.now()


class MockResponse:
    def __init__(self):
        self.status_code = 200

    @staticmethod
    def json() -> dict:
        return {"mock_info": "mock"}


def test_fetch_forecast_job(mocker):
    data: dict = {"mock_info": "mock"}
    status_code: int = 200

    def mock_execute() -> tuple:
        return (MockResponse(), CURRENT_TIMESTAMP)

    mocker.patch(
        "app.jobs.fetch_forecast_job.FetchForecastJob.execute",
        mock_execute
    )

    response: Response
    timestamp: datetime
    response, timestamp = FetchForecastJob.execute()

    assert response.json() == data
    assert response.status_code == status_code
    assert timestamp == CURRENT_TIMESTAMP
