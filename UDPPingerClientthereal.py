from datetime import datetime
from socket import *
from time import time

serverName = '10.252.100.56'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = raw_input('Message:')
c = 10
i = 1
#v = (10 - 1)
r = 9
dt = datetime.now()
dt2 = datetime.now()
et = dt - dt2
print c, 'pings are being tried.\n'
while i < c:
        i+= 1
	r-= 1
	#dt = datetime.now()
	#dt2 = datetime.now()
	et = (dt - dt2)
        print '\nPing attempt number', i, 'is currently in progress.\n'
        print r, 'attempts remain.\n'
	#print v, 'attempts remain.\n
        clientSocket.sendto(message,(serverName,serverPort))
        clientSocket.settimeout(10)

        print message
        print 'Time Elapsed: ', et.microseconds, 'microseconds\n'
        message, address = clientSocket.recvfrom(2048)
timeout
print 'Request Timed Out! '
#while i <= 10:
    #print counter, 'pings are being tried.\n'
    #while i < counter:
        #i+= 1
    #print '\nPing attempt number', i, 'is currently in progress.\n'
    #print remain, 'attempts remain.\n'
    #dt = datetime.now()
    #clientSocket.sendto(message,(serverName,serverPort))
    #clientSocket.settimeout(1)

    #print message
    #print 'Time Elapsed: ', et.microseconds, 'microseconds\n'
    #message, address = clientSocket.recvfrom(2048)
    #dt2 = datetime.now()
    ##et = dt - dt2;
    #timeout
    #print 'Request Timed Out! '
#else:
clientSocket.close()
#pass
#if __name__ == '__main__':
        #main()
