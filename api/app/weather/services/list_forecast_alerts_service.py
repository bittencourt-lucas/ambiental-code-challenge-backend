from decouple import config
from google.cloud.firestore_v1 import Client
from google.oauth2 import service_account

CREDENTIALS_FILE = config("GOOGLE_APPLICATION_CREDENTIALS")


class ListForecastAlertsService:
    @staticmethod
    def execute():
        client: Client = create_session()

        current_reading = client.collection("openmeteo").document(
            "current_reading").get().to_dict()

        if (current_reading is None):
            raise LookupError("No value retrieved.")

        return filter_only_alerts(current_reading)


def create_session() -> Client:
    credentials = service_account.Credentials.from_service_account_file(
        CREDENTIALS_FILE)
    return Client(credentials=credentials)


def filter_only_alerts(current_reading: dict) -> dict:
    return {
        "ultima_consulta": current_reading["ultima_consulta"],
        "dados": [entry for entry in current_reading["dados"] if entry["alerta"] is True]
    }
