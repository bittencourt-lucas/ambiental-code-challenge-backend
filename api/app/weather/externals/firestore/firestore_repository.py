from app.weather.repositories.abstract_repository import WeatherRepository
from app.weather.helpers.utils import filter_only_alerts


class FirestoreRepository(WeatherRepository):
    def __init__(self, client) -> None:
        self.client = client

    def list_forecast(self) -> dict:
        current_reading = self.client.collection("openmeteo").document(
            "current_reading").get().to_dict()

        if (current_reading is None):
            raise LookupError("No value retrieved.")

        return current_reading

    def list_alerts(self) -> dict:
        current_reading = self.client.collection("openmeteo").document(
            "current_reading").get().to_dict()

        if (current_reading is None):
            raise LookupError("No value retrieved.")

        return filter_only_alerts(current_reading)
