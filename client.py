#client.py

import socket
def readFile(name):
    f= open(name,"r")
    lines=f.read().strip().split("\n")
    message=""
    for line in lines:
        message+=str(line)+" "
    f.close()
    return message
def interprateData(message):
    row=[]
    board=[]
    count=0
    mess=message.split()
    print message
    for i in range(64):
        if i%8==0 and i!=0:
            board.append(row)
            row=[]
        row.append(mess[i-1])
    board.append(row)

    return board
def Main(s):
    
##    while message != 'q':
    while True:
        data = s.recv(2048)
        print data
        if data!="":
            break
    print "message recevived"
    return interprateData(data)
def sendMessage(s):
    message = readFile("arrangement2.txt")
    s.send(message)
    return Main(s)

    
##        print 'Received from server: ' + str(data)
        
##    s.close()


