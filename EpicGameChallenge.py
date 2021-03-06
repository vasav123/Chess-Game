#Chess Game
from pygame import *
from Piece import *
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
    for y in range(8):
        for x in range(8):
            if lst[y][x].getOValue()!="0":
                win.blit(lst[y][x].getImage(),(lst[y][x].getX()*(h/8),lst[y][x].getY()*(h/8)))
    
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
def checkIfCheckMate(board):
    whiteIsStillPlaying=False
    blackIsStillPlaying=False
    for y in range (8):
        for x in range(8):
            if board[y][x].getValue()=="white king":
                whiteIsStillPlaying=True
            if board[y][x].getValue()=="black king":
                blackIsStillPlaying=True
    if blackIsStillPlaying==False:
        return [True,"white"]
    if whiteIsStillPlaying==False:
        return [True,"black"]
    return [False,"no winner"]
def writeFile(board,name):
    f=open(name)
def restart():
    global board,move_count,state
    board= readFile("arrangement.txt")
    move_count=0
    state="thinking"
    for y in range(8):
        for x in range(8):
            board[y][x].setDangered(board,True) 
running=True
screen= display.set_mode((600,600))
board= readFile("arrangement.txt")
h=600
move_count=0
state="thinking"
for y in range(8):
    for x in range(8):
        board[y][x].setDangered(board,True)

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
                elif move_count%2==0 and  board[y1][x1].getColour()=="white" and (mx/(h/8),my/(h/8)) in board[y1][x1].showPossibleMoves(board):
                    movePiece(board,state,mx,my,h)
                    move_count+=1
                    state="thinking"
                elif move_count%2==1 and  board[y1][x1].getColour()=="black" and (mx/(h/8),my/(h/8)) in board[y1][x1].showPossibleMoves(board):
                    movePiece(board,state,mx,my,h)
                    move_count+=1
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
    if checkIfCheckMate(board)[0]:
        screen.blit(image.load(checkIfCheckMate(board)[1]+".png"),(0,0))
        draw.rect(screen,(0,0,0),Rect(170,460,240,70),1)
        if Rect(170,460,240,70).collidepoint(mx,my) and mb[0]:
            restart()
    display.flip()
quit()
