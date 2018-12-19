class BTreeKey:
    def __init__(self,key,filePosition,rightSon,leftSon,ownNode):
        self.key = key
        self.filePosition = filePosition
        self.rightSon = rightSon
        self.leftSon = leftSon
        self.ownNode = ownNode

    def atLeaf(self):        
        return self.leftSon is None and self.rightSon is None

    def getOwnNode(self):
        return self.ownNode

    def getRightSon(self):
        return self.rightSon

    def getLeftSon(self):
        return self.leftSon

    def setRightSon(self,node):
        self.rightSon = node

    def setLeftSon(self,node):
        self.leftSon = node

    def getFilePosition(self):
        return self.filePosition

    def getKey(self):
        return self.key
      
