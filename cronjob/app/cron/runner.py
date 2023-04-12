from crontab import CronTab


class JobRunner:
    def __init__(self):
        self.cron: CronTab = CronTab(user=True)

    def create_job(self, command: str, recurrency: str):
        self.job = self.cron.new(command=command)
        self.job.setall(recurrency)

    def start(self):
        self.cron.write()
