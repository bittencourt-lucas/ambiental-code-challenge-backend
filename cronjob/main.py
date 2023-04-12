
from app.cron.runner import JobRunner


runner = JobRunner()
runner.create_job(
    command="/home/lbittencourt/Documentos/Coding/ambiental-code-challenge-backend/cronjob/venv/bin/python3 /home/lbittencourt/Documentos/Coding/ambiental-code-challenge-backend/cronjob/app/cron/fetch_forecast_job.py", recurrency="* * * * *")
runner.start()
