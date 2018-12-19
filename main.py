import TDAFile
import Buffer
import Bitacora
import Item
import PartidaGuardada
import Personaje

file = TDAFile.TDAFile("test.txt")
file.openFile()


bufferPersonajes = Buffer.Buffer("MetadataFile.txt",0)

Manrique = Personaje.Personaje("bryan",1,1,1)
bufferPersonajes.setActualObject(Manrique)
file.insert(bufferPersonajes)

Manrique = Personaje.Personaje("juan",10,10,10)
bufferPersonajes.setActualObject(Manrique)
file.insert(bufferPersonajes)

Manrique = Personaje.Personaje("ernesto",421,1,1)
bufferPersonajes.setActualObject(Manrique)
file.insert(bufferPersonajes)

Manrique = Personaje.Personaje("pablo",412,1,1)
bufferPersonajes.setActualObject(Manrique)
file.insert(bufferPersonajes)

Manrique = Personaje.Personaje("asldjsa",423,1,1)
bufferPersonajes.setActualObject(Manrique)
file.insert(bufferPersonajes)

Manrique = Personaje.Personaje("mmmmm",422,1,1)
bufferPersonajes.setActualObject(Manrique)
file.insert(bufferPersonajes)

Manrique = Personaje.Personaje("jjuuu",43,1,1)
bufferPersonajes.setActualObject(Manrique)
file.insert(bufferPersonajes)

Manrique = Personaje.Personaje("asldjsa",8,1,1)
bufferPersonajes.setActualObject(Manrique)

objectttt = file.find(bufferPersonajes)
if objectttt is not None:
    print (objectttt[1].getDamage())
file.closeFile()



