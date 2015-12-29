from Piece import *
class AiEngine:
    def __init__(self):
        ""
    def searchTree(self,node,depth,a,b,m):
        if depth==0 or node.getTerminal():
            return node.evalBoard()
        if m:
            bestValue=-10000
            for child in node.getChildren():
                bestValue=max(bestValue,self.searchTree(child,depth-1,a,b,False))
                a=max(a,bestValue)
                if b<=a:
                    break
##            node.setValue(bestValue)
            return bestValue
        else:
            bestValue=10000
            for child in node.getChildren():
                bestValue=min(bestValue,self.searchTree(child,depth-1,a,b,True))
                bb=min(b,bestValue)
                if b<=a:
                    break
##            node.setValue(bestValue)
            return bestValue

class Node:
    def __init__(self,b,parent):
        self.parent=parent
        self.board=b
        self.children=[]
    def evalBoard(self):
        wvalue=0
        bvalue=0
        for y in range(8):
            for x in range(8):
                if self.board[y][x].getColour()=="white":
                    wvalue+=board[y][x].getPValue()
                elif self.board[y][x].getColour()=="black":
                    bvalue+=board[y][x].getPValue()
        return wvalue-bvalue
    
    def getTerminal(self):
        if len(self.children)==0:
            return True
        else:
            return False

    def getBoard(self):
        return self.board
    
    def moveBoard(self,x1,y1,x2,y2):
        self.board[y2][x2]=self.board[y1][x1]
        print self.board[y1][x1].getOValue()+" has been moved to "+str(x2)+","+str(y2)
        self.board[y1][x1]=Piece("0",x1,y1,False,False,False)
        
    def getChildren(self):
        return self.children
    
    def addChild(self,node):
        self.children.append(node)
    def getParent(self):
        return self.parent
def movePiece(board,y1,x1,x2,y2):
    board[y1][x1].setMoved(True)
    for y in range(8):
        for x in range(8):
            board[y][x].setDangered(board,False)
            
    if board[y1][x1].getType()=="king" and x2-x1==2 and board[y1][x1].getColour()=="white":
           board[y1][x1].setCord(x2,y2)
           board[y2][x2]=board[y1][x1]
           board[y1][x1]=Piece("0",x1,y1,False,False,False)                       
           board[7][7].setCord(5,7)
           board[7][5]=board[7][7]
           board[7][7]=Piece("0",7,7,False,False,False)
    elif board[y1][x1].getType()=="king" and x1-x2==2 and board[y1][x1].getColour()=="white":
           board[y1][x1].setCord(x2,y2)
           board[y2][x2]=board[y1][x1]
           board[y1][x1]=Piece("0",x1,y1,False,False,False)                       
           board[7][0].setCord(3,7)
           board[7][3]=board[7][0]
           board[7][0]=Piece("0",0,7,False,False,False)
    elif board[y1][x1].getType()=="king" and x1-x2==2 and board[y1][x1].getColour()=="black":
           board[y1][x1].setCord(x2,y2)
           board[y2][x2]=board[y1][x1]
           board[y1][x1]=Piece("0",x1,y1,False,False,False)                       
           board[0][0].setCord(3,0)
           board[0][3]=board[0][0]
           board[0][0]=Piece("0",0,0,False,False,False)
    elif board[y1][x1].getType()=="king" and x2-x1==2 and board[y1][x1].getColour()=="black":
           board[y1][x1].setCord(x2,y2)
           board[y2][x2]=board[y1][x1]
           board[y1][x1]=Piece("0",x1,y1,False,False,False)
           board[0][7].setCord(5,0)
           board[0][5]=board[0][7]
           board[0][7]=Piece("0",0,7,False,False,False)
    else:
        board[y1][x1].setCord(x2,y2)
        board[y2][x2]=board[y1][x1]
        board[y1][x1]=Piece("0",x1,y1,False,False,False)
    
    for y in range(8):
        for x in range(8):
            board[y][x].setDangered(board,True)
##    board[my/(h/8)][mx/(h/8)].promote(screen)
    return board
def makeTree(iNode,depth):
    if depth==0:
        return
    else:
        print depth
        for y in range(8):
            for x in range(8):
                if depth%2==0 and iNode.getBoard()[y][x].getColour()=="white" and iNode.getBoard()[y][x].getOValue()!="0":
                    for move in iNode.getBoard()[y][x].showPossibleMoves(iNode.getBoard()):
                        newBoard=movePiece(iNode.getBoard(),x,y,move[0],move[1])
                        newNode=Node(newBoard,iNode)
                        iNode.addChild(newNode)
                        makeTree(newNode,depth-1)
                elif depth%2==1 and iNode.getBoard()[y][x].getColour()=="black" and iNode.getBoard()[y][x].getOValue()!="0":
                    for move in iNode.getBoard()[y][x].showPossibleMoves(iNode.getBoard()):
                        newBoard=movePiece(iNode.getBoard(),x,y,move[0],move[1])
                        newNode=Node(newBoard,iNode)
                        iNode.addChild(newNode)
                        makeTree(newNode,depth-1)
def readFile(name):
    f= open(name,"r")
    lines=f.read().strip().split("\n")
    values=[]
    x=0
    y=0
    for l in lines:
##        print l
        pces=l.split(" ")
        v=[]
        x=0
##        print
        for p in pces:
            
            v.append(Piece(p,x,y,False,False,False))
            x+=1
        values.append(v)
        y+=1
    f.close()
    return values
board=readFile("arrangement.txt")
board2=readFile("arrangement.txt")


initialNode=Node(board,None)

makeTree(initialNode,3)


def printBoard(xboard):
    for y in range(8):
        for x in range(8):
            print xboard[y][x].getOValue(),
        print 

def printTree(initialNode,depth):
    if depth==0 or initialNode.getTerminal():        
        return None

    for node in initialNode.getChildren():
        printBoard(node.getBoard())
        printTree(node,depth-1)
printBoard (initialNode.getChildren()[0].getChildren()[5].getBoard())
##print initialNode
##printTree(initialNode,2)

##initialnode=Node(0)
##n1=Node(0)
##n2=Node(0)
##n3=Node(2)
##n4=Node(7)
##n5=Node(1)
##n6=Node(8)
##initialnode.addChild(n1)
##initialnode.addChild(n2)
##n1.addChild(n3)
##n1.addChild(n4)
##n2.addChild(n5)
##n2.addChild(n6)
##x=AiEngine()
##print x.searchTree(initialNode,2,10000,-10000,True)
##for y in range(8):
##    for x in range(8):
##        print board2[y][x].getOValue()+" ",
##    print
