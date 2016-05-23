import time
time1=time.time()
time2=time.time()
a = 1
while True:
    time2=time.time()
    print str(round(time2 - time1, 2)) + " seconds"
    time.sleep(.1)



