from app.weather.services.list_forecast_service import ListForecastService
from app.weather.helpers.mocked_data.stored_data import data
from app.weather.repositories.in_memory.in_memory_repository import InMemoryRepository


def test_list_forecast_service():
    in_memory_weather_repository = InMemoryRepository()
    list_alerts_service = ListForecastService(in_memory_weather_repository)

    output = list_alerts_service.execute()

    assert output == data
