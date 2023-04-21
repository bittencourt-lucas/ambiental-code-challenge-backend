import json
from decouple import config
from google.cloud.firestore_v1 import Client
from google.oauth2 import service_account

CREDENTIALS_FILE = config("GOOGLE_APPLICATION_CREDENTIALS")
with open(CREDENTIALS_FILE, "r", encoding="utf-8") as file:
    CREDENTIALS_INFO = file.read()
    file.close()


def create_session() -> Client:
    credentials = service_account.Credentials.from_service_account_info(
        json.loads(CREDENTIALS_INFO, strict=False))
    return Client(credentials=credentials)
