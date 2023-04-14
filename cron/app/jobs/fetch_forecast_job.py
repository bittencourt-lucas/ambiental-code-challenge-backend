from httpx import get, Response

OPEN_METEO_URL: str = "https://api.open-meteo.com/v1/forecast"
PRAIA_DE_JOAQUINA_PARAMS: dict = {
    "latitude": "-27.6289",
    "longitude": "-48.4478",
    "hourly": "windspeed_180m,winddirection_180m"
}

class FetchForecastJob:
    @staticmethod
    def execute():    
        response: Response = get(url=OPEN_METEO_URL, params=PRAIA_DE_JOAQUINA_PARAMS)
        print(response.text)

