import os
from crontab import CronTab


if __name__ == "__main__":
    NEXT_AT_MINUTE_5 = "5 * * * *"

    venv_path = os.path.dirname(
        os.path.abspath(__file__)) + "/venv/bin/python3"
    runner_file = os.path.dirname(
        os.path.abspath(__file__)) + "/app/runner.py"

    cron = CronTab(user=True)
    job = cron.new(command=f"{venv_path} {runner_file}")
    job.setall(NEXT_AT_MINUTE_5)
    cron.write()
