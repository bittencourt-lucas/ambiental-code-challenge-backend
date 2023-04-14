from typing import Tuple
from decouple import config
from google.cloud.firestore_v1 import Client
from google.oauth2 import service_account
from httpx import Response
from datetime import datetime

CREDENTIALS_FILE: str = config("GOOGLE_APPLICATION_CREDENTIALS")


class StoreInFirestoreJob:
    @staticmethod
    def execute(data: dict) -> None:
        client: Client = create_session()

        client.collection("openmeteo").document("current_reading").set(
            dict({"ultima_consulta": data["ultima_consulta"], "dados": data["dados"]}))


def create_session() -> Client:
    credentials = service_account.Credentials.from_service_account_file(
        CREDENTIALS_FILE)
    return Client(credentials=credentials)
