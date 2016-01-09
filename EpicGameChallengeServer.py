#Chess Game
from pygame import *
from Piece import *
import server
import client
from socket import *
def checkIfUserWantsToMovePiece(win,h,mx,my,mb):
   
    x=mx/(h/8)
    y=my/(h/8)
    
    if (board[y][x].getValue()!="blank" and mb[0]==1) :
        board[y][x].drawMovesPossible(board,win,h)
        draw.rect(win,(0,200,50),Rect(board[y][x].getX()*(h/8),board[y][x].getY()*(h/8),h/8,h/8),10)       
    return (x,y)

def clickedAtSamePos(Px,Py,Cx,Cy,h):
    return (Px,Py)==(Cx/(h/8),Cy/(h/8))

   
def drawBoard(win,h):
    '''
    Draws the board
    '''
    for i in range(8):
        for j in range(8):
            if (j%2==0 and i%2==0) or  (j%2==1 and i%2==1):
                draw.rect(win,(240,240,240),Rect(i*(h/8),j*(h/8),h/8,h/8),0)
            elif (j%2==1 and i%2==0) or(j%2==0 and i%2==1):
                draw.rect(win,(0,200,50),Rect(i*(h/8),j*(h/8),h/8,h/8),0)

def putPieces(win,lst,h):
    ''' Temporary draws the pieces according to the board
    '''
    colours= {"w1":(0,0,155),"w2":(137,123,175),"w3":(99,81,146),"w4":(67,47,117),"w5":(40,22,87),"w6":(21,6,58),"b1":(155,0,0),"b2":(212,106,106),"b3":(170,57,57),"b4":(128,21,21),"b5":(85,0,0),"b6":(117,6,58)}
    for y in range(8):
        for x in range(8):
            if lst[y][x].getOValue()!="0":
                draw.circle(win,colours[lst[y][x].getOValue()],(lst[y][x].getX()*(h/8)+h/16,lst[y][x].getY()*(h/8)+h/16),h/16)
    
def readFile(name):
    f= open(name,"r")
    lines=f.read().strip().split("\n")
    values=[]
    x=0
    y=0
    for l in lines:
        pces=l.split(" ")
        v=[]
        x=0
        for p in pces:
            v.append(Piece(p,x,y,False,False,False))
            x+=1
        values.append(v)
        y+=1
    f.close()
    return values
def makeBoard(board):
    values=[]
    x=0
    y=0
    for l in board:
        v=[]
        x=0
        for p in l:
            v.append(Piece(p,x-1,y,False,False,False))
            x+=1
        values.append(v)
        y+=1
##    f.close()
    return values
def movePiece(board,state,mx,my,h):
    board[y1][x1].setMoved(True)
    
    for y in range(8):
        for x in range(8):
            board[y][x].setDangered(board,False)
            
    if board[y1][x1].getType()=="king" and mx/(h/8)-x1==2 and board[y1][x1].getColour()=="white":
           board[y1][x1].setCord(mx/(h/8),my/(h/8))
           board[my/(h/8)][mx/(h/8)]=board[y1][x1]
           board[y1][x1]=Piece("0",x1,y1,False,False,False)                       
           board[7][7].setCord(5,7)
           board[7][5]=board[7][7]
           board[7][7]=Piece("0",7,7,False,False,False)
    elif board[y1][x1].getType()=="king" and x1-mx/(h/8)==2 and board[y1][x1].getColour()=="white":
           board[y1][x1].setCord(mx/(h/8),my/(h/8))
           board[my/(h/8)][mx/(h/8)]=board[y1][x1]
           board[y1][x1]=Piece("0",x1,y1,False,False,False)                       
           board[7][0].setCord(3,7)
           board[7][3]=board[7][0]
           board[7][0]=Piece("0",0,7,False,False,False)
    elif board[y1][x1].getType()=="king" and x1-mx/(h/8)==2 and board[y1][x1].getColour()=="black":
           board[y1][x1].setCord(mx/(h/8),my/(h/8))
           board[my/(h/8)][mx/(h/8)]=board[y1][x1]
           board[y1][x1]=Piece("0",x1,y1,False,False,False)                       
           board[0][0].setCord(3,0)
           board[0][3]=board[0][0]
           board[0][0]=Piece("0",0,0,False,False,False)
    elif board[y1][x1].getType()=="king" and mx/(h/8)-x1==2 and board[y1][x1].getColour()=="black":
           board[y1][x1].setCord(mx/(h/8),my/(h/8))
           board[my/(h/8)][mx/(h/8)]=board[y1][x1]
           board[y1][x1]=Piece("0",x1,y1,False,False,False)
           board[0][7].setCord(5,0)
           board[0][5]=board[0][7]
           board[0][7]=Piece("0",0,7,False,False,False)
    else:
        board[y1][x1].setCord(mx/(h/8),my/(h/8))
        board[my/(h/8)][mx/(h/8)]=board[y1][x1]
        board[y1][x1]=Piece("0",x1,y1,False,False,False)
    
    for y in range(8):
        for x in range(8):
            board[y][x].setDangered(board,True)
    board[my/(h/8)][mx/(h/8)].promote(screen)
##    state="thinking"

def writeFile(board,name):
    f=open(name,"w")
    for row in board:
        message=""
        for p in row:
            message+=p.getOValue()+" "
##        message=message[0::16]
        message+="\n"
        f.write(message)
    f.close()
    
def sendData(board,user,c):
    writeFile(board,"arrangement2.txt")
    if user=="s":
        newBoard=makeBoard(server.Main(c))
        print"data received"
    if user=="c":
        newBoard=makeBoard(client.Main(c))
        print"data received"
    return newBoard
def reciveData(user,c):
    data = c.recv(1024)
    newBoard=server.interperaateData(data)
    
running=True
screen= display.set_mode((600,600))
board= readFile("arrangement.txt")
h=600
move_count=0
state="thinking"
user="s"
for y in range(8):
    for x in range(8):
        board[y][x].setDangered(board,True)
if user=="s":
    host = '127.0.0.1'
    port = 5000

    s = socket()
    s.bind((host,port))

    s.listen(1)
    c, addr = s.accept()
    print "Connection from: " + str(addr)
elif user=="c":
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.connect((host, port))
    
while running:
    for e in event.get():
        if e.type==QUIT:
            running=False
        
        if e.type==MOUSEBUTTONDOWN:
            if state=="thinking":
                state="picking"
            elif state=="picking":
                if clickedAtSamePos(x1,y1,mx,my,h):
                    state="thinking"
                elif board[y1][x1].getColour()=="white" and (mx/(h/8),my/(h/8)) in board[y1][x1].showPossibleMoves(board):
                    movePiece(board,state,mx,my,h)
                    drawBoard (screen,600)
                    putPieces(screen,board,600)
                    display.update()
                    board=sendData(board,"s",c)
                    state="thinking"
                else:
                    state="picking"
    drawBoard (screen,600)
    putPieces(screen,board,600)
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    if state=="thinking":
        x1,y1= checkIfUserWantsToMovePiece(screen,h,mx,my,mb)
    elif state=="picking":
        board[y1][x1].drawMovesPossible(board,screen,h)
        draw.rect(screen,(0,200,50),Rect(board[y1][x1].getX()*(h/8),board[y1][x1].getY()*(h/8),h/8,h/8),10)
    display.flip()
if user=="s":
    c.close()
elif user=="c":
    s.close()
quit()
