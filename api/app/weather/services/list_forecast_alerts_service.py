from google.cloud.firestore_v1 import Client


class ListForecastAlertsService:
    @staticmethod
    def execute(client: Client):
        current_reading = client.collection("openmeteo").document(
            "current_reading").get().to_dict()

        if (current_reading is None):
            raise LookupError("No value retrieved.")

        return filter_only_alerts(current_reading)


def filter_only_alerts(current_reading: dict) -> dict:
    return {
        "ultima_consulta": current_reading["ultima_consulta"],
        "dados": [entry["data"] for entry in current_reading["dados"] if entry["alerta"] is True]
    }
