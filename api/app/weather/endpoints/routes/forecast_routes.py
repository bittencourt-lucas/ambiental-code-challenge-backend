from fastapi import APIRouter
from app.shared.database.firestore.client import create_session
from app.weather.endpoints.controllers.forecast_controller import ForecastController

client = create_session()

forecast_controller = ForecastController(client)

forecast_router = APIRouter()


@forecast_router.get("/previsao")
def list_forecast() -> dict:
    return forecast_controller.list_forecast()


@forecast_router.get("/alerta")
def list_forecast_alerts() -> dict:
    return forecast_controller.list_forecast_alerts()
