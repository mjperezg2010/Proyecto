#/******************************************************
#Nombre de la clase: TDAFile
#
#Descripcion:        Plantilla de las operaciones elem-
#                    entales de un archivo.
#
#Clase:              Estructura de Datos II
#
#Fecha:              9 de diciembre del 2018
#
#Autor:              Bryan Manrique Amador Mena
#******************************************************/

import os
import Buffer
import BTreeNode
import BTreeKey

class TDAFile:
    def __init__(self,fileName):
        self.fileName = fileName        
        self.root = None
        self.ALfileName = fileName[:-4]+"AVL.txt"
        self.INFfileName = fileName[:-4]+"INF.txt"
        self.availListFile = open(self.ALfileName,'w')
        self.indexFile = open(self.INffileName,'w')        
        self.indexFile.close()
        self.availListFile.close()
        self.auxiliaryStr = ""

    def createFile(self,fileName):
        self.file = open(fileName,'w')
        self.file.close()
        
    def createFile(self):
        self.file = open(self.fileName,'w')
        self.file.close()        

    def openFile(self):
        self.file = open(self.fileName,'a+')    

    def closeFile(self):
        self.file.close()

    def deleteFile(self):
        os.remove(fileName)

    def getFile(self):
        return self.file

    def loadBTree(self):
        self.indexFile = open(INFfileName,'r')        
        objectList = indexFile.read().split(";")
        self.indexFile.close()
        self.root = None
        for i in range (0,len(objectList)):
            str1 = objectList[i]
            aux = str1.split(",")
            toInsertKey = aux[0]
            pointerPosition = int(aux[1])
            buffer
            if self.root is None:            
                newKey = BTreeKey.BTreeKey(toInsertKey,0,None,None,self.root)
                self.root = BTreeNode.BTreeNode(True,True,None,newKey)            
            else:            
                actualNode = self.root
                if actualNode.isLeaf and actualNode.getNumKeys() < 2:
                    actualNode.addKey(BTreeKey.BTreeKey(toInsertKey,pointerPosition,None,None,actualNode))
                else:
                    while not actualNode.isLeaf and actualNode is not None:   
                        if actualNode.getNumKeys() == 1:
                            if actualNode.getKey(0).getKey() > toInsertKey:                    
                                actualNode = actualNode.getKey(0).getLeftSon()
                            else:
                                actualNode = actualNode.getKey(0).getRightSon()
                        elif actualNode.getNumKeys() == 2:
                            if actualNode.getKey(0).getKey() > toInsertKey:                    
                                actualNode = actualNode.getKey(0).getLeftSon()
                            elif actualNode.getKey(0).getKey() < toInsertKey and actualNode.getKey(1).getKey() > toInsertKey:
                                actualNode = actualNode.getKey(0).getRightSon()                    
                            else:
                                actualNode = actualNode.getKey(1).getRightSon()
                        else:
                            if actualNode.getKey(0).getKey() > toInsertKey:                    
                                actualNode = actualNode.getKey(0).getLeftSon()
                            elif actualNode.getKey(0).getKey() < toInsertKey and actualNode.getKey(1).getKey() > toInsertKey:
                                actualNode = actualNode.getKey(0).getRightSon()
                            elif actualNode.getKey(1).getKey() < toInsertKey and actualNode.getKey(2).getKey() > toInsertKey:
                                actualNode = actualNode.getKey(1).getRightSon()                                        
                            else:                    
                                actualNode = actualNode.getKey(2).getRightSon()     
                                                                    
                    if actualNode.isLeaf and actualNode.getNumKeys() < 2:
                        actualNode.addKey(BTreeKey.BTreeKey(toInsertKey,pointerPosition,None,None,actualNode))
                    else:
                        self.seekNode(actualNode,toInsertKey,pointerPosition)

    def appendIndexFileInfo(self,key):        
        self.auxiliaryStr += key+";"

    def saveIndexFile(self):
        self.indexFile = open(self.INFfileName,'w')
        indexFile.write(auxiliaryStr)
        self.indexFile.close()

    def fileSize(self,file):
        string = file.read()
        return len(string)

    def getFreeSpace(self):
        self.availListFile = open(self.ALfileName,'r')
        data = self.availListFile.read().split(",")
        self.availListFile.close()
        if len(data) != 0:
            return int(data[0])
        else:
            return -1

    def insert(self,buffer):
        pointerPosition = self.getFreeSpace()
        if pointerPosition != -1:
            self.file.seek(pointerPosition)    
            buffer.write(self.file)
            self.appendIndexFileInfo(buffer.getActualObjectKey()+","+pointerPosition)
        else:
            pointerPosition = self.fileSize(self.file)
            self.file.seek(pointerPosition)
            buffer.write(self.file)
            toInsertKey = buffer.getActualObjectKey()
            self.appendIndexFileInfo(toInsertKey+","+pointerPosition)
        if self.root is None:            
            newKey = BTreeKey.BTreeKey(toInsertKey,0,None,None,self.root)
            self.root = BTreeNode.BTreeNode(True,True,None,newKey)            
        else:            
            actualNode = self.root
            if actualNode.isLeaf and actualNode.getNumKeys() < 2:
                actualNode.addKey(BTreeKey.BTreeKey(buffer.getActualObjectKey(),pointerPosition,None,None,actualNode))
            else:
                while not actualNode.isLeaf and actualNode is not None:   
                    if actualNode.getNumKeys() == 1:
                        if actualNode.getKey(0).getKey() > toInsertKey:                    
                            actualNode = actualNode.getKey(0).getLeftSon()
                        else:
                            actualNode = actualNode.getKey(0).getRightSon()
                    elif actualNode.getNumKeys() == 2:
                        if actualNode.getKey(0).getKey() > toInsertKey:                    
                            actualNode = actualNode.getKey(0).getLeftSon()
                        elif actualNode.getKey(0).getKey() < toInsertKey and actualNode.getKey(1).getKey() > toInsertKey:
                            actualNode = actualNode.getKey(0).getRightSon()                    
                        else:
                            actualNode = actualNode.getKey(1).getRightSon()
                    else:
                        if actualNode.getKey(0).getKey() > toInsertKey:                    
                            actualNode = actualNode.getKey(0).getLeftSon()
                        elif actualNode.getKey(0).getKey() < toInsertKey and actualNode.getKey(1).getKey() > toInsertKey:
                            actualNode = actualNode.getKey(0).getRightSon()
                        elif actualNode.getKey(1).getKey() < toInsertKey and actualNode.getKey(2).getKey() > toInsertKey:
                            actualNode = actualNode.getKey(1).getRightSon()                                        
                        else:                    
                            actualNode = actualNode.getKey(2).getRightSon()     
                                                                
                if actualNode.isLeaf and actualNode.getNumKeys() < 2:
                    actualNode.addKey(BTreeKey.BTreeKey(buffer.getActualObjectKey(),pointerPosition,None,None,actualNode))
                else:
                    self.seekNode(actualNode,toInsertKey,pointerPosition)
    
    def seekNode(self,node,key,pointerPosition):        
        if node.getNumKeys() == 2:            
            newKey = BTreeKey.BTreeKey(key,pointerPosition,None,None,node)
            node.addKey(newKey)
            toPromoveKey = node.getKey(1)
            toPromoveKey.setLeftSon(BTreeNode.BTreeNode(False,node.getKey(0).atLeaf(),toPromoveKey.getOwnNode(),node.getKey(0)))
            toPromoveKey.setRightSon(BTreeNode.BTreeNode(False,node.getKey(2).atLeaf(),toPromoveKey.getOwnNode(),node.getKey(2)))
            if toPromoveKey.getOwnNode().getFather() == None:
                self.root = BTreeNode.BTreeNode(True,False,None,toPromoveKey)                                
            else:                
                self.seekNode(toPromoveKey.getOwnNode().getFather(),toPromoveKey,pointerPosition)

    def update(self,buffer):
        position = find(buffer)[0]
        if position != -1:
            self.file.seek(position)
            buffer.write(self.file)
        else:
            self.file.seek(self.file.tell())
            buffer.write(self.file)

    def find(self,buffer):     
        actualNode = self.root
        toFindKey = buffer.getActualObjectKey()
        while actualNode is not None:
            positionKey = actualNode.contains(toFindKey)            
            if positionKey != -1:                
                self.file.seek(actualNode.getKey(positionKey).getFilePosition())                
                return [positionKey,buffer.read(self.file)]
            else:
                if actualNode.getNumKeys() == 1:
                    if actualNode.getKey(0).getKey() > toFindKey:                    
                        actualNode = actualNode.getKey(0).getLeftSon()
                    else:
                        actualNode = actualNode.getKey(0).getRightSon()
                elif actualNode.getNumKeys() == 2:
                    if actualNode.getKey(0).getKey() > toFindKey:                    
                        actualNode = actualNode.getKey(0).getLeftSon()
                    elif actualNode.getKey(0).getKey() < toFindKey and actualNode.getKey(1).getKey() > toFindKey:
                        actualNode = actualNode.getKey(0).getRightSon()                    
                    else:
                        actualNode = actualNode.getKey(1).getRightSon()
                else:
                    if actualNode.getKey(0).getKey() > toFindKey:                    
                        actualNode = actualNode.getKey(0).getLeftSon()
                    elif actualNode.getKey(0).getKey() < toFindKey and actualNode.getKey(1).getKey() > toFindKey:
                        actualNode = actualNode.getKey(0).getRightSon()
                    elif actualNode.getKey(1).getKey() < toFindKey and actualNode.getKey(2).getKey() > toFindKey:
                        actualNode = actualNode.getKey(1).getRightSon()                                        
                    else:                    
                        actualNode = actualNode.getKey(2).getRightSon()         
        return None
                        
    def deleteReg(self,buffer):
        toRemove = find(buffer)[0]
        if toRemove != -1:
            #self.indexFile = open(self.INFfileName,'a+')
            #aux = self.indexFile.read().split(";")            
            #newStr = ""
            #for i in range (0,len(aux)):
            #    str1 = aux[i].split(",")
            #    if str1[0] != buffer.getActualObjectKey():
            #        newStr += aux[i]+";"
            #self.indexFile.seek(0)
            #self.indexFile.write(newStr)
            #self.indexFile.close()
            #self.loadBTree()

            self.availListFile = open(self.ALfileName,'a+')
            self.availListFile.seek(self.fileSize(availListFile))
            self.availListFile.write(buffer.getFilePosition+",")
            self.availListFile.close()
            self.file.seek(toRemove)
            buffer.erase(self.file)

