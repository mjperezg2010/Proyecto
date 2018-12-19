import Personaje

class Buffer:
    def __init__(self,file,objectIndicator):
        #seeting metaData
        self.listAtributesSize = [9]
        self.objectIndicator = objectIndicator
        metaDataFile = open(file,"r")
        dataLine = metaDataFile.readlines(objectIndicator)
        infoObjectList = dataLine[0].split(",")
        self.numAtributes = int(infoObjectList[1])        
        for i in range(0,self.numAtributes+1):
            self.listAtributesSize.append(int(infoObjectList[i+2]))
        self.regSize = self.listAtributesSize[len(self.listAtributesSize)-1]    
        metaDataFile.close()
        self.objectList = []

    def setRootKey(self,key):
        self.rootKey = key

    def getObjectList(self):
        return self.objectList

    def getRootKey(self,key):
        self.rootKey = key

    def setActualObject(self,_object):
        self.actualObject = _object    

    def getActualObjectKey(self):
        return self.actualObject.getKey()

    def getRegSize(self):
        return self.regSize

    def readEverything(self,file):
        fileObject = file.getFile()
        fileObject.seek(0)
        dataLines = fileObject.readLines()
        for j in range (0,len(dataLines)):
            cont = 0
            indexFlag = 0
            atributes = [0,0,0,0,0,0,0,0,0]
            for i in range (0,self.numAtributes):
                atributes[cont] = dataLine[indexFlag:indexFlag+self.listAtributesSize[cont]]
                indexFlag = indexFlag+self.listAtributesSize[cont]
                cont += 1
                atributes[cont] = str(atributes[cont]).rstrip()            
            if self.objectIndicator == 0:            
                self.objectList.append(Personaje.Personaje(atributes[0],atributes[1],atributes[2],atributes[3]))
            elif self.objectIndicator == 1:
                self.objectList.append(PartidaGuardada.PartidaGuardada(atributes[0],atributes[1],atributes[2]))
            elif self.objectIndicator == 2:
                self.objectList.append(Bitacora.Bitacora(atributes[0],atributes[1],atributes[2],atributes[3],atributes[4]))
            else:
                self.objectList.append(Item.Item(atributes[0],atributes[1],atributes[2]))
        return self.objectList

    def read(self,file):        
        dataLine = file.read(self.regSize)        
        cont = 0
        indexFlag = 0
        atributes = [0,0,0,0,0,0,0,0,0]
        for i in range (0,self.numAtributes):
            atributes[cont] = dataLine[indexFlag:indexFlag+self.listAtributesSize[cont]]
            indexFlag = indexFlag+self.listAtributesSize[cont]
            cont += 1
            atributes[cont] = str(atributes[cont]).rstrip()            
        if self.objectIndicator == 0:            
            self.actualObject = Personaje.Personaje(atributes[0],atributes[1],atributes[2],atributes[3])
        elif self.objectIndicator == 1:
            self.actualObject = PartidaGuardada.PartidaGuardada(atributes[0],atributes[1],atributes[2])
        elif self.objectIndicator == 2:
            self.actualObject = Bitacora.Bitacora(atributes[0],atributes[1],atributes[2],atributes[3],atributes[4])
        else:
            self.actualObject = Item.Item(atributes[0],atributes[1],atributes[2])
        return self.actualObject

    def write(self,file):        
        if self.objectIndicator == 0:            
            file.write(self.actualObject.getNombre()+" "*( self.listAtributesSize[0]-len(self.actualObject.getNombre()) ) +
                str(self.actualObject.getDamage())+" "*( self.listAtributesSize[1]-len(str(self.actualObject.getDamage())) ) +
                str(self.actualObject.getDefense())+" "*( self.listAtributesSize[2]-len(str(self.actualObject.getDefense())) ) +
                str(self.actualObject.getVida())+" "*( self.listAtributesSize[3]-len(str(self.actualObject.getVida())) ) )
        elif self.objectIndicator == 1:
            file.write(self.actualObject.getNombrePartida()+" "*( self.listAtributesSize[0]-len(self.actualObject.getNombrePartida()) ) +
                self.actualObject.getMisionesCompletadas()+" "*( self.listAtributesSize[1]-len(self.actualObject.getMisionesCompletadas()) ) +
                self.actualObject.getArmadurasObtenidas()+" "*( self.listAtributesSize[2]-len(self.actualObject.getArmadurasObtenidas()) ) )                
        elif self.objectIndicator == 2:
            file.write(self.actualObject.getNombrePartida()+" "*( self.listAtributesSize[0]-len(self.actualObject.getNombrePartida()) ) +
                self.actualObject.getFecha()+" "*( self.listAtributesSize[1]-len(self.actualObject.getFecha()) ) +
                self.actualObject.getHoraEntrada()+" "*( self.listAtributesSize[1]-len(self.actualObject.getHoraEntrada()) ) +
                self.actualObject.getHoraSalida()+" "*( self.listAtributesSize[1]-len(self.actualObject.getHoraSalida()) ) +                
                self.actualObject.getHoraInsert()+" "*( self.listAtributesSize[3]-len(self.actualObject.getHoraInsert()) ) )
        else:
            file.write(self.actualObject.getNombre()+" "*( self.listAtributesSize[0]-len(self.actualObject.getNombre()) ) +
                self.actualObject.getNombreMonstruo()+" "*( self.listAtributesSize[1]-len(self.actualObject.getNombreMonstruo()) ) +
                self.actualObject.getTipo()+" "*( self.listAtributesSize[2]-len(self.actualObject.getTipo()) ) )
    
    def erase(self,file):
        file.write("$"*self.listAtributesSize[0])    
    