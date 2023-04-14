from typing import Tuple
from decouple import config
from google.cloud.firestore_v1 import Client
from google.oauth2 import service_account
from httpx import Response
from datetime import datetime
from app.runner.job_runner import JobRunner

CREDENTIALS_FILE: str = config("GOOGLE_APPLICATION_CREDENTIALS")


class StoreInFirestoreJob(JobRunner):
    @staticmethod
    def execute(data: Tuple[Response, datetime]) -> None:
        client: Client = create_session()

        response: Response
        timestamp: datetime
        response, timestamp = data

        client.collection("openmeteo").document("current_reading").set(
            dict({"time": timestamp, "data": response.json()}))


def create_session() -> Client:
    credentials = service_account.Credentials.from_service_account_file(
        CREDENTIALS_FILE)
    return Client(credentials=credentials)
