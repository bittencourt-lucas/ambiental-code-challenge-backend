from datetime import datetime, timedelta
from app.jobs.filter_forecast_job import FilterForecastJob

CURRENT_TIMESTAMP = datetime.now()


def test_filter_forecast_job():
    data_entry = {
        "hourly": {
            "time": [CURRENT_TIMESTAMP + timedelta(hours=num) for num in range(0, 5)],
            "windspeed_180m": [5, 25, 15, 20, 5],
            "winddirection_180m": [110, 120, 130, 140, 150],
        }
    }

    expected_output = {
        "ultima_consulta": CURRENT_TIMESTAMP,
        "dados": [
            {
                "data": CURRENT_TIMESTAMP + timedelta(hours=2),
                "vel": 15,
                "dir": 130,
                "alerta": False,
            },
            {
                "data": CURRENT_TIMESTAMP + timedelta(hours=3),
                "vel": 20,
                "dir": 140,
                "alerta": True,
            },
        ]
    }

    output = FilterForecastJob.execute((data_entry, CURRENT_TIMESTAMP))

    assert expected_output == output
