from decouple import config
from google.cloud.firestore_v1 import Client
from google.oauth2 import service_account

CREDENTIALS_FILE = config("GOOGLE_APPLICATION_CREDENTIALS")


def create_session() -> Client:
    credentials = service_account.Credentials.from_service_account_file(
        CREDENTIALS_FILE)
    return Client(credentials=credentials)
