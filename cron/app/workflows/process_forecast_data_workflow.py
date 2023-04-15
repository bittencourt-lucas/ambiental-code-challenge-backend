from jobs.fetch_forecast_job import FetchForecastJob
from jobs.filter_forecast_job import FilterForecastJob
from jobs.store_in_firestore_job import StoreInFirestoreJob


class ProcessForecastDataWorkflow:
    @staticmethod
    def run():
        forecast_data = FetchForecastJob.execute()
        formatted_data = FilterForecastJob.execute(forecast_data)
        StoreInFirestoreJob.execute(formatted_data)
