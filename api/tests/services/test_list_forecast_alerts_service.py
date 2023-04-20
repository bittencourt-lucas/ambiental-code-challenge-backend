from app.weather.services.list_forecast_alerts_service import ListForecastAlertsService
from app.weather.helpers.mocked_data.stored_data import data
from app.weather.helpers.utils import filter_only_alerts
from app.weather.repositories.in_memory.in_memory_repository import InMemoryRepository


def test_list_forecast_alerts_service():
    in_memory_weather_repository = InMemoryRepository()
    list_alerts_service = ListForecastAlertsService(in_memory_weather_repository)
    
    output = list_alerts_service.execute()

    expected_output = filter_only_alerts(data)

    assert output == expected_output
