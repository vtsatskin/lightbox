from datetime import datetime
from threading import Timer

x=datetime.today()
y=x.replace(day=x.day+1, hour=23, minute=55, second=0, microsecond=0)
delta_t=y-x

secs=delta_t.seconds+1

def hello_world():
    print "hello world"
    t2 = Timer(3600, hello_world)
    t2.start()   

t = Timer(secs, hello_world)
print secs
t.start()