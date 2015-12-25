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
            return [bestValue,node]
        else:
            bestValue=10000
            for child in node.getChildren():
                bestValue=min(bestValue,self.searchTree(child,depth-1,a,b,True))
                bb=min(b,bestValue)
                if b<=a:
                    break
##            node.setValue(bestValue)
            return [bestValue,node]

class Node:
    def __init__(self,board):
        self.board=board
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
        return bvalue-wvalue
    
    def getTerminal(self):
        if len(self.children)==0:
            return True
        else:
            return False

    def getBoard(self):
        return self.board
    
    def moveBoard(self,x1,y1,x2,y2):
        self.board[y2][x2]=self.board[y1][x1]
        
        self.board[y1][x1]=Piece("0",x1,y1,False,False,False)
        
    def getChildren(self):
        return self.children
    
    def addChild(self,node):
        self.children.append(node)
    
            

def makeTree(intialNode,board,depth):
    if depth==0:
        return
    else:
        for y in range(8):
            for x in range(8):
                for move in board[y][x].showPossibleMoves(board):
                    newNode=Node(board)
                    newNode.moveBoard(x,y,move[0],move[1])
                    initialNode.addChild(newNode)
                    makeTree(newNode,newNode.getBoard(),depth-1)
            
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
board=readFile("arrangement.txt")
initialNode=Node(board)


makeTree(initialNode,board,2)


    
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
x=AiEngine()
a,b= x.searchTree(initialNode,2,10000,-10000,True)
for y in range(8):
    for x in range(8):
        print b.getBoard()[y][x].getValue()+" ",
    print
