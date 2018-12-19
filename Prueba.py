from Monster import Monster

#30 el max, 25,20,15,10
monstruo=Monster("Rathalos",25,20,100) #30,30,100
#print (monstruo.getNombre()+" va a atacar con el ataque especial y su ataque es de:",monstruo.getDamage())

vidaHunter=100

defenseHunter=20 #25


"""vidaHunter=monstruo.AtaqueEspecial(vidaHunter,defenseHunter)
vidaHunter+=20 #30
vidaHunter=monstruo.AtaqueEspecial(vidaHunter,defenseHunter)
vidaHunter+=20 #30"""



while (vidaHunter>=0):
	print("Rathalos:",monstruo.getVida())
	print("Cazador:",vidaHunter)

	vidaHunter=monstruo.Ataque(vidaHunter,defenseHunter)

	if(vidaHunter<=0):
		break

	monstruo.setVida(monstruo.getVida()-(40-monstruo.getDefense()))  #55-30

	if(monstruo.getVida()<=0):
		break

	
	
	

print ("\nFInal")
print("Rathalos:",monstruo.getVida())
print("Cazador:",vidaHunter)


"""
import time

x=0

ListaPlantas=[]
while(x<5):
	ListaPlantas.append(Planta("Hierba",x))
	x=x+1

for i in range (0,len(ListaPlantas)):
	print(ListaPlantas[i].getNombre(),ListaPlantas[i].getNumero())


Guardando=time.strftime("%H:%M:%S")
print(type(Guardando))
Gur=time.strftime("%d/%m/%y") 
print(Gur)


##Probando
horaEntrada=time.strftime("%H:%M:%S")
print ("Escribi mierda")
time.sleep(1)
horaInsert=time.strftime("%H:%M:%S")
time.sleep(1)
total = 40+45

from PartidaGuardada import PartidaGuardada
from Item import Item
from Bitacora import Bitacora

save=PartidaGuardada("Partida Magistral",["1","2"])

for i in range(0,len(save.getMisionesCompletadas())):
	print(save.getMisionesCompletadas()[i])

item1=Item("Colmillo de Rathalos","Rathalos","Material")
item2=Item("Lengua de Rathalos","Rathalos","Material")
item3=Item("Hongo","Paloumun","Planta")

print(item1.getNombre(),item1.getTipo(),item1.getNombreMonstruo())
print(item2.getNombre(),item2.getTipo(),item2.getNombreMonstruo())
print(item3.getNombre(),item3.getTipo(),item3.getNombreMonstruo())

print("\n")

bitacora=Bitacora("partida Magistral",time.strftime("%d/%m/%y"),horaEntrada,time.strftime("%H:%M:%S"),horaInsert)

print(bitacora.getNombrePartida(),bitacora.getFecha(),bitacora.getHoraEntrada(),bitacora.getHoraSalida(),bitacora.getHoraInsert())
#nombrePartida,fecha,horaEntrada,horaSalida,horaInsert"""