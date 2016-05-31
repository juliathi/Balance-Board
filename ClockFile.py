import time

Sec = 0
Min = 0

while True:

    Sec += 1
    secClock = (str(Min) + " Mins " + str(Sec) + " Sec ")
    print secClock
    time.sleep(1)
    if Sec == 60:
        Sec = 0
        Min += 1
        clock = (str(Min) + " Minute")
        print(clock)