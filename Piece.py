from pygame import *
class Piece:
    '''
        This is used to keep track of each pieces values and moves it can do
    '''
    def __init__(self,number,x,y,d1,d2,moved):
        self.originalvalue=number
        if number[0]=="w":
            self.colour ="white"
            pvalue={"1":"pawn","2":"rook","3":"horse","4":"bishop","5":"queen","6":"king"}
            self.value=pvalue[number[1]]
        elif number[0]=="b":
            self.colour="black"
            pvalue={"1":"pawn","2":"rook","3":"horse","4":"bishop","5":"queen","6":"king"}
            self.value=pvalue[number[1]]
        else:
            self.colour="blank"
            self.value=""
        self.x=x
        self.y=y
        self.dangerb=d1
        self.dangerw=d2
        self.moved=moved
    def getMovesPossible(self):
        '''
        This is used to determine what moves are availabe to the certain piece. 
        '''
        horizontalrow=[]
        horizontalrow1=[]
        verticalrow=[]
        verticalrow1=[]
        rdiagonal=[]
        rdiagonal1=[]
        ldiagonal=[]
        ldiagonal1=[]
        for i in range(-1,-9,-1):
            horizontalrow1.append((i,0))
            verticalrow1.append((0,i))
            rdiagonal1.append((i,i))
            ldiagonal1.append((-i,i))
            
        for i in range (1,9):
            horizontalrow.append((i,0))
            verticalrow.append((0,i))
            rdiagonal.append((i,i))
            ldiagonal.append((-i,i))
        movespossible={"pawn":[[(0,1)]],"rook":[horizontalrow,horizontalrow1,verticalrow,verticalrow1],"bishop":[rdiagonal,rdiagonal1,ldiagonal,ldiagonal1],
                       "queen":[horizontalrow,horizontalrow1,verticalrow,verticalrow1,rdiagonal,rdiagonal1,ldiagonal,ldiagonal1],
                            "king":[[(0,1)],[(0,-1)],[(1,0)],[(-1,0)],[(-1,-1)],[(-1,1)],[(1,1)],[(1,-1)]],
                            "horse":[[(-1,2)],[(-2,1)],[(1,2)],[(2,1)],[(2,-1)],[(1,-2)],[(-1,-2)],[(-2,-1)]],
                            "":[[]]}
        if self.value!="pawn":
            return movespossible[self.value]
        else:
            if self.colour=="black":
                if self.y==1:
                    return [[(0,1),(0,2)]]
                else:
                    return [[(0,1)]]
            if self.colour=="white":
                if self.y==6:
                    return [[(0,-1),(0,-2)]]
                else:
                    return [[(0,-1)]]        

        
    def showPossibleMoves(self,board):
        '''
        This checks if the move available are actual possible moves and ensures there is nothing in the way and stuff
        '''
        moves=self.getMovesPossible()
        actualpossiblemoves=[]
        if self.value=="":
            return []
        if self.value=="pawn":
            if self.colour=="black":
                nx=self.x+1
                ny=self.y+1
                if nx>=0 and nx<8 and ny>=0 and ny<8  and board[ny][nx].getColour()=="white":
                    moves.append([(1,1)])
                nx=self.x-1
                ny=self.y+1
                if nx>=0 and nx<8 and ny>=0 and ny<8  and board[ny][nx].getColour()=="white":
                    moves.append([(-1,1)])
            if self.colour=="white":
                nx=self.x+1
                ny=self.y-1
                if nx>=0 and nx<8 and ny>=0 and ny<8  and board[ny][nx].getColour()=="black":
                    moves.append([(1,-1)])
                nx=self.x-1
                ny=self.y-1
                if nx>=0 and nx<8 and ny>=0 and ny<8  and board[ny][nx].getColour()=="black":
                    moves.append([(-1,-1)])
        if self.value=="king":
            if self.colour=="white" and self.getMoved()==False and board[7][5].getDanger()[0]==False and board[7][6].getDanger()[0]==False and board[7][7].getMoved()==False:
                moves[2].append((2,0))
            if self.colour=="white" and self.getMoved()==False and board[7][4].getDanger()[0]==False and board[7][3].getDanger()[0]==False and board[7][2].getDanger()[0]==False and board[0][7].getMoved()==False:
                moves[3].append((-2,0))
            if self.colour=="black" and self.getMoved()==False and board[0][5].getDanger()[1]==False and board[0][6].getDanger()[1]==False and board[0][7].getMoved()==False:
                moves[3].append((-2,0))
            if self.colour=="black" and self.getMoved()==False and board[0][4].getDanger()[1]==False and board[0][3].getDanger()[1]==False and board[0][2].getDanger()[1]==False and board[0][7].getMoved()==False:
                moves[2].append((2,0))

            
        for row in moves:
            for i in row:
                x1=i[0]+self.x
                y1=i[1]+self.y
                if x1>=0 and x1<8 and y1>=0 and y1<8:
                    pieceatpos=board[y1][x1]
                    if pieceatpos.getColour()!=self.colour:
                        if pieceatpos.getColour()=="blank":
                            actualpossiblemoves.append((x1,y1))
                        else:
                            if self.value=="pawn" and i[0]==0:
                                break
                            actualpossiblemoves.append((x1,y1))
                            break                   
                    else:
                        break
        return actualpossiblemoves
    
    def setDangered(self,board,tf):
        moves=self.showPossibleMoves(board)
        if self.value=="pawn":
            moves=[]
            if self.colour=="black":
                nx=self.x+1
                ny=self.y+1
                if nx>=0 and nx<8 and ny>=0 and ny<8:
                    moves.append((self.x+1,self.y+1))
                nx=self.x-1
                ny=self.y+1
                if nx>=0 and nx<8 and ny>=0 and ny<8:
                    moves.append((self.x-1,self.y+1))
            if self.colour=="white":
                nx=self.x+1
                ny=self.y-1
                if nx>=0 and nx<8 and ny>=0 and ny<8:
                    moves.append((self.x+1,self.y-1))
                nx=self.x-1
                ny=self.y-1
                if nx>=0 and nx<8 and ny>=0 and ny<8:
                    moves.append((self.x-1,self.y-1))
        for (x,y) in moves:
            board[y][x].setDanger(tf,self.x,self.y,board)
    def promote(self,win):
        if self.value=="pawn" and self.colour=="black" and self.y==7:
            self.value=self.getNewValue(win)
        elif self.value=="pawn" and self.colour=="white" and self.y==0:            
            self.value= self.getNewValue(win)
    def getNewValue(self,win):
        choices=[(0,300,100,100),(110,300,100,100),(220,300,100,100),(330,300,100,100)]
        values=["queen","horse","bishop","rook"]
        running=True
        while running:
            for e in event.get():
                if e.type==QUIT:
                    running=False
            mx,my=mouse.get_pos()
            mb=mouse.get_pressed()
            win.fill((255,255,255))
            for i in choices:
                draw.rect(win,(200,0,0),Rect(i),0)
            for i in range(4):
                if Rect(choices[i]).collidepoint(mx,my) and mb[0]==1:
                    running=False
                    return values[i]
            display.update()
                
    def drawMovesPossible(self,board,win,h):
        '''
        This just draws the moves possible
        '''
        possiblemoves=self.showPossibleMoves(board)
        for i in possiblemoves:
            draw.rect(win,(255,0,0),Rect((i[0])*h/8,(i[1])*(h/8),h/8,h/8),4)
##    def movePiece(self,board,x2,y2):
##        self.kingCastle(board,x2,y2)
##        self.setCord(x2,y2)
##        board[y2][x2]=self
##        return Piece("0",self.x,self.y,False,False,False)
##    def kingCastle(self,board,x2,y2):
##        if board[self.y][self.x].getType()=="king" and x2-self.x==2 and self.getColour()=="white":
##               board[self.y][self.x].setCord(x2,y2)
##               board[y2][x2]=board[self.y][self.x]
##               board[self.y][self.x]=Piece("0",self.x,self.y,False,False,False)                       
##               board[7][7].setCord(5,7)
##               board[7][5]=board[7][7]
##               board[7][7]=Piece("0",7,7,False,False,False)
##        elif board[self.y][self.x].getType()=="king" and self.x-x2==2 and self.getColour()=="white":
##               board[self.y][self.x].setCord(x2,y2)
##               board[y2][x2]=board[self.y][self.x]
##               board[self.y][self.x]=Piece("0",self.x,self.y,False,False,False)                       
##               board[7][0].setCord(3,7)
##               board[7][3]=board[7][0]
##               board[7][0]=Piece("0",0,7,False,False,False)
##        elif board[self.y][self.x].getType()=="king" and self.x-x2==2 and self.getColour()=="black":
##               board[self.y][self.x].setCord(x2,y2)
##               board[y2][x2]=board[self.y][self.x]
##               board[self.y][self.x]=Piece("0",self.x,self.y,False,False,False)                       
##               board[0][0].setCord(3,0)
##               board[0][3]=board[0][0]
##               board[0][0]=Piece("0",0,0,False,False,False)
##        elif board[self.y][self.x].getType()=="king" and x2-self.x==2 and self.getColour()=="black":
##               board[self.y][self.x].setCord(x2,y22)
##               board[y2][x2]=board[self.y][self.x]
##               board[self.y][self.x]=Piece("0",self.x,self.y,False,False,False)
##               board[0][7].setCord(5,0)
##               board[0][5]=board[0][7]
##               board[0][7]=Piece("0",0,7,False,False,False)
##        
#########################################################################################

    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getValue(self):
        return self.colour+" "+self.value
    def getPValue(self):
        valuesofpieces={"pawn":1,"rook":5,"horse":3,"bishop":3,"queen":9,"king":20}
        return valuesofpieces[self.value]
    def getColour(self):
        return self.colour
    def getOValue(self):
        return self.originalvalue
    def getDanger(self):
        return (self.dangerb,self.dangerw)
    def getMoved(self):
        return self.moved
    def getType(self):
        return self.value
    def setCord(self,x,y):
        self.x=x
        self.y=y
    def setDanger(self,tf,x,y,board):
        if board[y][x].colour=="black" :
            self.dangerb=tf
        elif board[y][x].colour=="white":
            self.dangerw=tf
    def setMoved(self,x):
        self.moved=x
        
##########################################################################################
