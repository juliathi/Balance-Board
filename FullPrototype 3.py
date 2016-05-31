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

    TCP_IP = '10.2.172.184'
    IP_PORT = 55558

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    IP = client_socket.connect((TCP_IP, IP_PORT))

#school = client_socket.connect((SCHOOL_TCP_IP, SCHOOL_IP_PORT))

    Min = 0
    time1 = time.time()
    time2 = time.time()
    a = 1
    while True:
        time2 = time.time()
        print str(Min) + " min " + str(round(time2 - time1, 2)) + " seconds"
        if time2 - time1 >= 59:
            time1 = time.time()
            time2 = time.time()
            Min += 1

        time.sleep(.25)

        data = client_socket.recv(1000)

        if ():
            split = data.split(',')
            axisY = split[6]
            client_socket.close()

            break

        else:

            split = data.split(',')
            split6 = (round(float(split[6]), 3))
            print ("Weight Placement (L+ R-): " + str(split6))
            print ('\n')

        if float(split6) >= float(0.3):
            print("Finished")
            break

        if float(split6) <= float(-0.3):
            print("Finished")
            break

results = []
results.append(ID_number + ", " + str(Min) + " min " + str(round(time2 - time1, 2)) + " seconds")
print results

if newResponse == "no":
    time.sleep(1)
    print "Bye!"