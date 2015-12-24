class AiEngine:
    def __init__(self):
        ""
    def searchTree(self,node,depth,a,b,m):
        if depth==0 or node.getTerminal():
            return node.getValue()
        if m:
            bestValue=-10000
            for child in node.getChildren():
                bestValue=max(bestValue,self.searchTree(child,depth-1,a,b,False))
                a=max(a,bestValue)
                if b<=a:
                    break
            node.setValue(bestValue)
            return bestValue
        else:
            bestValue=10000
            for child in node.getChildren():
                bestValue=min(bestValue,self.searchTree(child,depth-1,a,b,True))
                bb=min(b,bestValue)
                if b<=a:
                    break
            node.setValue(bestValue)
            return bestValue

class Node:
    def __init__(self,board):
        self.board=board
        self.children=[]
        
    def evalBoard(self):
        wvalue=0
        bvalue=0
        for y in range(8):
            for x in range(8):
                if board[y][x].getColour=="white":
                    wvalue+=board[y][x].getValue()
                else:
                    bvalue+=board[y][x].getValue()
        return bvalue-wvalue
    
    def getTerminal(self):
        if len(self.children)==0:
            return True
        else:
            return False

    def getBoard(self):
        return self.board
    
    def getChildren(self):
        return self.children
    
    def addChild(self,node):
        self.children.append(node)
    
    def makeAMove(self,move):
            

def makeTree():
    n=Node(board,)
    
initialnode=Node(0)
n1=Node(0)
n2=Node(0)
n3=Node(2)
n4=Node(7)
n5=Node(1)
n6=Node(8)
initialnode.addChild(n1)
initialnode.addChild(n2)
n1.addChild(n3)
n1.addChild(n4)
n2.addChild(n5)
n2.addChild(n6)
x=AiEngine()
print x.searchTree(initialnode,2,10000,-10000,True)
print initialnode.getValue()
