from app.jobs.fetch_forecast_job import FetchForecastJob
from app.jobs.format_forecast_job import FormatForecastJob
from app.jobs.store_in_firestore_job import StoreInFirestoreJob


forecast_data = FetchForecastJob.execute()
formatted_data = FormatForecastJob.execute(forecast_data)
StoreInFirestoreJob.execute(formatted_data)
