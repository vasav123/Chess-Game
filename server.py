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
def Main(c):
##    host = '127.0.0.1'
##    port = 5000
##
##    s = socket.socket()
##    s.bind((host,port))
##
##    s.listen(1)
##    c, addr = s.accept()
##    print "Connection from: " + str(addr)
    c.send(readFile("arrangement2.txt"))
    print "message sent"
    while True:
        print"hey"
        data = c.recv(1024)
##        print "from connected user: " + str(data)
        if data!="":
            break
    
##        data = str(data).upper()
##        print "sending: " + str(data)
    print "message recv"
    return interprateData(data)

##if __name__ == '__main__':
##    interprateData(readFile("arrangement.txt"))


