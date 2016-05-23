#base code from http://stackoverflow.com/questions/27594926/python-start-and-stop-timer
import time

start = time.time()
end = time.time()
while True:
    end = time.time()
    print str(round(end - start, 2)) + "  Seconds"
    time.sleep(0.25)