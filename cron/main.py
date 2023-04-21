import os
from crontab import CronTab
from decouple import config


if __name__ == "__main__":
    NEXT_AT_MINUTE_5 = "5 * * * *"

    credentials = config("GOOGLE_APPLICATION_CREDENTIALS")
    command_env = config("COMMAND_ENV")
    output = config("OUTPUT_PARAMETERS")

    runner_file = os.path.dirname(
        os.path.abspath(__file__)) + "/app/runner.py"

    cron = CronTab(user=True)
    job = cron.new(
        pre_comment=True,
        comment="START CRONTAB",
        command=f"{command_env} {runner_file} {output}")
    job.env["GOOGLE_APPLICATION_CREDENTIALS"] = credentials
    job.env["COMMAND_ENV"] = command_env
    job.env["OUTPUT_PARAMETERS"] = output
    job.setall(NEXT_AT_MINUTE_5)
    cron.write()
