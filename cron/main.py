from app.jobs.fetch_forecast_job import FetchForecastJob


forecast_data = FetchForecastJob.execute()
print(forecast_data.json())
