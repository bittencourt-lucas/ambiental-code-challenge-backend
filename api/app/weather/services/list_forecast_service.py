from app.weather.repositories.abstract_repository import WeatherRepository


class ListForecastService:
    def __init__(self, repository: WeatherRepository):
        self.repository = repository

    def execute(self) -> dict:
        return self.repository.list_forecast()
