from app.weather.services.list_forecast_service import ListForecastService
from app.weather.services.list_forecast_alerts_service import ListForecastAlertsService
from app.weather.externals.firestore.firestore_repository import FirestoreRepository


class ForecastController:
    def __init__(self, client):
        self.repository = FirestoreRepository(client)

    def list_forecast(self) -> dict:
        list_forecast_service = ListForecastService(self.repository)
        return list_forecast_service.execute()

    def list_forecast_alerts(self) -> dict:
        list_forecast_alerts_service = ListForecastAlertsService(
            self.repository)
        return list_forecast_alerts_service.execute()
