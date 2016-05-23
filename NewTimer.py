import time
time1=time.time()
time2=time.time()

while True:
    time.sleep(.25)
    time2=time.time()
    print (time2 - time1)
    time1=time2