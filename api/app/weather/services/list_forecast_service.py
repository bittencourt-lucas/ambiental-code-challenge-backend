from decouple import config
from google.cloud.firestore_v1 import Client
from google.oauth2 import service_account

CREDENTIALS_FILE = config("GOOGLE_APPLICATION_CREDENTIALS")


class ListForecastService:
    @staticmethod
    def execute():
        client: Client = create_session()

        current_reading = client.collection("openmeteo").document(
            "current_reading").get().to_dict()

        if (current_reading is None):
            raise LookupError("No value retrieved.")

        return current_reading


def create_session() -> Client:
    credentials = service_account.Credentials.from_service_account_file(
        CREDENTIALS_FILE)
    return Client(credentials=credentials)
