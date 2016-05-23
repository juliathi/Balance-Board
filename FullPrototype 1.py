#USE DM ON SENSORLOG
import time
import socket
ID_number = raw_input("What's your student ID? ")
response = raw_input("Are you ready(Y/N)? ")
newResponse = response.lower()

if newResponse == "yes" or newResponse == "y" or newResponse == "ye":
    print int(3)
    time.sleep(1)
    print int(2)
    time.sleep(1)
    print int(1)
    time.sleep(1)
    print "GO!"
    time.sleep(1)

    TCP_IP = '10.2.172.121'
    IP_PORT = 58615

    Sec = 0
    Min = 0

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    IP = client_socket.connect((TCP_IP, IP_PORT))

#school = client_socket.connect((SCHOOL_TCP_IP, SCHOOL_IP_PORT))
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

        data = client_socket.recv(1000)

        if ():
            split = data.split(',')
            axisY = split[6]
            client_socket.close()

            break

        else:

            split = data.split(',')
            split6 = (round(float(split[6]),3))
            print split6

        if float(split6) >= float(0.3):
            print("Finished")
            time.sleep(0.5)
            print ('\n')
            print (ID_number + "; " + str(Min) + " min " + str(Sec) + " sec")
            break

        if float(split6) <= float(-0.3):
            print("Finished")
            time.sleep(0.5)
            print ('\n')
            print (ID_number + "; " + str(Min) + " min " + str(Sec) + " sec")
            break


if newResponse == "no":
    time.sleep(1)
    print "Bye!"
