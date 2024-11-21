import sched
import time

class Scheduler:
    def __init__(self):
        self.scheduler = sched.scheduler(time.time, time.sleep)

    def schedule_task(self, interval: int, action, actionargs=()):
        self.scheduler.enter(interval, 1, self.schedule_task, (interval, action, actionargs))
        action(*actionargs)

    def run(self):
        self.scheduler.run()
