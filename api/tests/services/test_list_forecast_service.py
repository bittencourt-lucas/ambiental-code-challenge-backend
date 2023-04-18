from tests.helpers.stored_data import data
from app.weather.services.list_forecast_service import ListForecastService


def test_list_forecast_service(mocker):
    def mock_execute() -> dict:
        return data

    mocker.patch(
        "app.weather.services.list_forecast_service.ListForecastService.execute",
        mock_execute
    )

    output = ListForecastService.execute()

    expected_output = data

    assert output == expected_output
