from google.cloud.firestore_v1 import Client


class ListForecastService:
    @staticmethod
    def execute(client: Client):
        current_reading = client.collection("openmeteo").document(
            "current_reading").get().to_dict()

        if (current_reading is None):
            raise LookupError("No value retrieved.")

        return current_reading
