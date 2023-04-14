from app.jobs.fetch_forecast_job import FetchForecastJob
from app.jobs.filter_forecast_job import FilterForecastJob
from app.jobs.store_in_firestore_job import StoreInFirestoreJob


forecast_data = FetchForecastJob.execute()
formatted_data = FilterForecastJob.execute(forecast_data)
StoreInFirestoreJob.execute(formatted_data)
