from tests.helpers.stored_data import data
from app.weather.services.list_forecast_alerts_service import ListForecastAlertsService, filter_only_alerts


def test_list_forecast_alerts_service(mocker):
    def mock_execute() -> dict:
        return filter_only_alerts(data)

    mocker.patch(
        "app.weather.services.list_forecast_alerts_service.ListForecastAlertsService.execute",
        mock_execute
    )

    output = ListForecastAlertsService.execute()

    expected_output = filter_only_alerts(data)

    assert output == expected_output
