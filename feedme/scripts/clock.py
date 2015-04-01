__author__ = 'oahayder'

import os
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon', hour=2)
def refresh_database():
    os.system("sync_data.py")

sched.start()
