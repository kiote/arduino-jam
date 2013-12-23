from apscheduler.scheduler import Scheduler
import httplib

sched = Scheduler()

@sched.interval_schedule(minutes=10)
def timed_job():
    conn = httplib.HTTPConnection("arduino-jam.herokuapp.com")
    conn.request("GET", "/")
    r1 = conn.getresponse()
    print r1.status

sched.start()

while True:
    pass


