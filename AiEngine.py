class AiEngine:
    def __init__(self):
        ""
    def searchTree(self,node,depth,m):
        if depth==0 or node.getTerminal():
            return node.getValue()
        if m:
            bestValue=-10000
        else:
            bestValue=10000
        for child in node.getChildren():
            val=self.searchTree(child,depth-1, not m)
            if m:
                bestValue=max(bestValue, val)
            else:
                bestValue=min(bestValue,val)
        node.setValue(bestValue)
        return bestValue

class Node:
    def __init__(self,value):
        self.value=value
        self.children=[]
        
    def getTerminal(self):
        if len(self.children)==0:
            return True
        else:
            return False
    def setValue(self,value):
        self.value=value
    def getValue(self):
        return self.value

    def getChildren(self):
        return self.children

    def addChild(self,node):
        self.children.append(node)
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
print x.searchTree(initialnode,2,True)
print initialnode.getValue()
