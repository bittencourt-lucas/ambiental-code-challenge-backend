import os
import ast
from httpx import get, Response
from typing import Optional

OPEN_METEO_URL: str = "https://api.open-meteo.com/v1/forecast"
PRAIA_DE_JOAQUINA_PARAMS: dict = {
    "latitude": "-27.6289",
    "longitude": "-48.4478",
    "hourly": "windspeed_180m,winddirection_180m"
}

class OpenMeteoClient:
    def __init__(self, params: Optional[dict]):
        self.params = params

    def get(self) -> dict:
        response: Response = get(url=OPEN_METEO_URL, params=self.params)
        decoded_content: str = response.content.decode("UTF-8")
        content: dict = ast.literal_eval(decoded_content)
        return content


client = OpenMeteoClient(params=PRAIA_DE_JOAQUINA_PARAMS)
data: dict = client.get()

with open(os.path.join("/home/lbittencourt/Documentos/Coding/ambiental-code-challenge-backend/cronjob/test.txt"), "a") as f:
    f.write(str(data) + '\n')
