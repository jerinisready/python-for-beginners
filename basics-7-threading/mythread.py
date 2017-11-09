import time
from random import randint
from threading import Thread
from datetime import datetime
def mySleepingFunc(sleep_for,i):
    print "Started Thread %d for %d sec\t\t%s" % (i,sleep_for,datetime.now())
    time.sleep(sleep_for)
    print "Ending Thread %d\t\t\t\t%s" % (i,datetime.now())

for i in range(6):
    random_time = randint(3,20)
    t = Thread(target=mySleepingFunc, args=(random_time,i))
    t.start()
