from app.weather.repositories.abstract_repository import WeatherRepository


class FirestoreRepository(WeatherRepository):
    def __init__(self, client) -> None:
        super().__init__(client)

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

        return self.filter_only_alerts(current_reading)

    def filter_only_alerts(self, current_reading: dict) -> dict:
        return {
            "ultima_consulta": current_reading["ultima_consulta"],
            "dados": [entry["data"] for entry in current_reading["dados"] if entry["alerta"] is True]
        }
