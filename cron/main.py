from app.jobs.fetch_forecast_job import FetchForecastJob
from app.jobs.store_in_firestore_job import StoreInFirestoreJob


forecast_data = FetchForecastJob.execute()
StoreInFirestoreJob.execute(forecast_data)
