from fastapi import APIRouter
from app.weather.endpoints.routes.forecast_routes import forecast_router

root_router = APIRouter()

root_router.include_router(forecast_router)
