from apscheduler.scheduler import Scheduler

sched = Scheduler()

@sched.interval_schedule(minutes=10)
def timed_job():
    print 'This job is run every three minutes.'

sched.start()

while True:
    pass


