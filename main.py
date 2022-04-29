from apscheduler.schedulers.blocking import BlockingScheduler

from src import init_pipeline
from src.helpers.log import LOGGER



sched = BlockingScheduler()

@sched.scheduled_job('interval', days=6)
def sched_job():
    LOGGER.info('>>Starting Scheduled Pipeline Job<<')
    init_pipeline()

sched.start()
