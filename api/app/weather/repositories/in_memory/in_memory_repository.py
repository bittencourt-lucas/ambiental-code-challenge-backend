from app.weather.repositories.abstract_repository import WeatherRepository
from app.weather.helpers.mocked_data.stored_data import data
from app.weather.helpers.utils import filter_only_alerts


class InMemoryRepository(WeatherRepository):
    forecast: dict = data

    def list_forecast(self) -> dict:
        return self.forecast

    def list_alerts(self) -> dict:
        return filter_only_alerts(self.forecast)
