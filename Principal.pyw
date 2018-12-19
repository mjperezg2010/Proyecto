#Proyecto inicio
#------------------------------------Librerias--------------------------
import tkinter as tk
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from Monster import Monster
from Hunter import Hunter
from Item import Item
from random import randint
import time # Esto es para el sleep, se usa time.sleep("El tiempo")
from Buffer import Buffer
from TDAFile import TDAFile
from PartidaGuardada import PartidaGuardada



#Cosas que faltan
#Bitacora
#Guardar partida y abrir partida
#Arbol

#------------------------------Ventanas------------------------------------
	

def pantallaJuegoAbrir():

	global listaMonstruos,noMision

	#------------------Cerrar Ventana Principal--------------------------------
	root1.state(newstate='withdraw')

	#-------------------Abrir nueva ventana----------------------------------
	pantallaJuego=tk.Toplevel()  #Si la quiero hacer hija y que se cierra temporalmente es tk.Toplevel() para eso impor tkinter as tk
	pantallaJuego.config(bg="#0E6655",width=700,height=500)
	pantallaJuego.iconbitmap("rathalos_grande.ico")

	#-----------------------Widgets de la ventana---------------------------


		

	#--Fondo--#
	labelTitulo=Label(pantallaJuego,bg="#0E6655") ##2ECC71
	imagen=PhotoImage(file="Monster-Hunter-World.png")
	labelTitulo.config(image=imagen)
	labelTitulo.grid(row=0,column=0,rowspan=25,columnspan=25)

	#--Labesls--#
	labelSeleccione=Label(pantallaJuego,text="Seleccione una mision",bg="#0F924E",fg="white")
	labelSeleccione.grid(row=0,column=0)


		#--Combo Box de las misiones--#
	cbMisiones=ttk.Combobox(pantallaJuego,width=30,state="readonly")
	listaTempMonstruos=[]

	for i in range(0,len(listaMonstruos)):
		listaTempMonstruos.append(listaMonstruos[i].getNombre())


	cbMisiones['values']=listaTempMonstruos
	cbMisiones.grid(row=1,column=0)

	botonActualizar=Button(pantallaJuego,text="Actualizar Misiones",bg="#0F924E",fg="white",width=14,command=lambda:actualizarcbMisiones(cbMisiones))
	botonActualizar.grid(row=1,column=1)


	textFieldNombre=Entry(pantallaJuego)
	textFieldNombre.grid(row=3,column=0)
	boton=Button(pantallaJuego,command=lambda:nombreHunter(textFieldNombre),text="Seleccionar nombre cazador")
	boton.grid(row=3,column=1)

	#--Menu--#
	barraMenu=Menu(pantallaJuego)
	pantallaJuego.config(menu=barraMenu)

	archivoMenu1=Menu(barraMenu,tearoff=0)
	barraMenu.add_cascade(label="Archivo",menu=archivoMenu1)
	archivoMenu1.add_command(label="Abrir",command=abrirArchivo)
	archivoMenu1.add_command(label="Guardar",command=guardarArchivo)
	archivoMenu1.add_separator()
	archivoMenu1.add_command(label="Salir")

	#--Botones--#

	botonMisiones=Button(pantallaJuego,text="Misiones",bg="black",fg="white",width=14,command=lambda:ventanaMisiones(cbMisiones))
	botonMisiones.grid(row=1,column=23)
	botonInventario=Button(pantallaJuego,text="Forja",bg="black",fg="white",width=14,command=tienda)
	botonInventario.grid(row=4,column=23)
	botonBaul=Button(pantallaJuego,text="Baul de Objetos",bg="black",fg="white",width=14,command=mirarInventario)
	botonBaul.grid(row=3,column=23)
	botonArmadura=Button(pantallaJuego,text="Armadura",bg="black",fg="white",width=14,command=escogerArmadura)
	botonArmadura.grid(row=2,column=23)
	botonCreacionMonstruos=Button(pantallaJuego,text="Creador",bg="black",fg="white",width=14,command=ventanaCreador)
	botonCreacionMonstruos.grid(row=5,column=23)
	botonMisionesCompletadas=Button(pantallaJuego,text="Misiones Completadas",bg="black",fg="white",width=14)


	#---------------------------Fin-------------------------------------

	
	pantallaJuego.mainloop()


def ventanaMisiones(cbMisiones):
	global armorPrincipal

	if(cbMisiones.get()==""):
		messagebox.showinfo("Advertencia!","No escogio ninguna mision")
	elif(armorPrincipal==""):
		messagebox.showinfo("Advertencia!","No escogio ninguna Armadura")
	else:
		noMision=False
		ventana=tk.Toplevel()
		ventana.title("Monster Hunter")
		ventana.iconbitmap("rathalos_grande.ico")


		#--Fondo--#
		fondo=Label(ventana)
		imagen=PhotoImage(file="PantallaJuego.png")
		fondo.config(image=imagen)
		fondo.grid(row=0,column=0,rowspan=30,columnspan=30)

		


		#--Variables para la pelea--
		
		global hunter
		global monstruo
		global listaMonstruos
		hunter.setVida(100)
		hunter.setDamage(20)
		monstruo.setVida(100)

		if (armorPrincipal=="Nergigante Armor"):
			hunter.setDefense(20)
			hunter.setDamage(40)	
		elif (armorPrincipal=="Paolumu Armor"):
			hunter.setDefense(5)
			hunter.setDamage(25)
		elif (armorPrincipal=="Rathalos Armor"):
			hunter.setDefense(10)
			hunter.setDamage(30)
		elif (armorPrincipal=="Kushala Daora Armor"):
			hunter.setDefense(15)
			hunter.setDamage(35)
		elif (armorPrincipal=="Kirin Armor"):
			hunter.setDefense(25)
			hunter.setDamage(45)
		elif (armorPrincipal=="Sin Armadura"):
			hunter.setDefense(0)
			hunter.setDamage(20)

		else:
			hunter.setDefense(0)
			hunter.setDamage(0)
			


		#Atributos monstruo

		monstruo=listaMonstruos[cbMisiones.current()]



		#Frame para el monstruo
		frameMonster=Frame(ventana)
		frameMonster.grid(row=7,column=29,rowspan=17)
		imagen2Label=Label(frameMonster,bg="#86BE84")
		nombreMonstruo=Label(ventana,bg="#86BE84")

		

		if(cbMisiones.get()=="Paolumu"):
			imagen3=PhotoImage(file="Paolumu.png")
			imagen2Label.config(image=imagen3)
			imagen2Label.pack()


			
		elif(cbMisiones.get()=="Rathalos"):
			imagen3=PhotoImage(file="Rathalos.png")
			imagen2Label.config(image=imagen3)
			imagen2Label.pack()
			
		elif(cbMisiones.get()=="Kushala Daora"):
			imagen3=PhotoImage(file="Kushala Daora.png")
			imagen2Label.config(image=imagen3)
			imagen2Label.pack()
			
		elif(cbMisiones.get()=="Nergigante"):
			imagen3=PhotoImage(file="Nergigante.png")
			imagen2Label.config(image=imagen3)
			imagen2Label.pack()
			
		elif(cbMisiones.get()=="Kirin"):
			imagen3=PhotoImage(file="Kirin.png")
			imagen2Label.config(image=imagen3)
			imagen2Label.pack()
			
		else: 
			imagen3=PhotoImage(file="Jinouga.png")
			imagen2Label.config(image=imagen3)
			imagen2Label.pack()
			

		nombreMonstruo.config(text=monstruo.getNombre())
		nombreMonstruo.grid(row=6,column=29)
		defenseLabelMonstruo=Label(ventana,text="Defensa: "+str(monstruo.getDefense()),bg="#86BE84")
		defenseLabelMonstruo.grid(row=16,column=28)
		vidaLabelMonstruo=Label(ventana,text="Vida: "+str(monstruo.getVida()),bg="#86BE84")
		vidaLabelMonstruo.grid(row=15,column=28)


		#Frame para poner al personaje
		frameHunter=Frame(ventana)
		frameHunter.grid(row=7,column=0,rowspan=17)

		#Label del framepersonaje
		labelArmadura=Label(frameHunter,bg="#86BE84")
		fileTemp=armorPrincipal+".png"

		if(fileTemp=="Sin Armadura.png" or fileTemp==".png"):
			fileTemp="Temporal Armor.png"
		imagen2=PhotoImage(file=fileTemp)
		labelArmadura.config(image=imagen2)
		labelArmadura.pack()

		#Label de los nombres y atributos
		nombre=Label(ventana,text=str(hunter.getNombre())+"\n"+"Armadura: "+armorPrincipal,bg="#86BE84")
		nombre.grid(row=6,column=0)
		defenseLabel=Label(ventana,text="Defensa: "+str(hunter.getDefense()),bg="#86BE84")
		defenseLabel.grid(row=16,column=1)
		vidaLabelHunter=Label(ventana,text="Vida: "+str(hunter.getVida()),bg="#86BE84")
		vidaLabelHunter.grid(row=15,column=1)


		#Progress bar de las vidas
		barraVidaHunter=ttk.Progressbar(ventana)
		barraVidaHunter.grid(row=24,column=0)
		barraVidaHunter.config(maximum=100)
		barraVidaHunter['value']=hunter.getVida()

		barraVidaMonstruo=ttk.Progressbar(ventana)
		barraVidaMonstruo.grid(row=24,column=29)
		barraVidaHunter.config(maximum=100)
		barraVidaMonstruo['value']=monstruo.getVida()


		#Labels que enseñan el ataque
		framePelea=Frame(ventana,bg="#86BE84")
		framePelea.grid(row=15,column=15,columnspan=7)
		lbPelea=Label(framePelea,text="Se ha avistado un "+monstruo.getNombre(),bg="#86BE84",width=34)
		lbPelea.pack()



		#Botones
		botonAtacar=Button(ventana,text="Atacar",command=lambda:Atacar(barraVidaHunter,barraVidaMonstruo,ventana,vidaLabelHunter,vidaLabelMonstruo,lbPelea),bg="#0F924E",fg="white",width=14)
		botonAtacar.grid(row=24,column=18,columnspan=7)

		#botonActualizar=Button(pantallaJuego,text="Actualizar Misiones",bg="#0F924E",fg="white",width=14,command=lambda:actualizarcbMisiones(cbMisiones))







		ventana.mainloop()


def escogerArmadura():
	ventanaArmadura=tk.Toplevel()
	ventanaArmadura.title("Monster Hunter")
	ventanaArmadura.iconbitmap("rathalos_grande.ico")

	fondo=Label(ventanaArmadura)
	imagen=PhotoImage(file="monster-hunter-world-2.png")
	fondo.config(image=imagen)
	fondo.grid(row=0,column=0,rowspan=30,columnspan=30)
	
	"""
	armadura=Frame(ventanaArmadura)
	armadura.grid(row=20,column=8)
	labelArmadura=Label(armadura,bg="#E0E1AE")
	imagen1=PhotoImage(file="Temporal Armor.png")
	labelArmadura.config(image=imagen1)
	labelArmadura.pack()
	"""


	""" listbox.insert(0, *listaArmaduras)
	listbox.selection_set(0)
	listbox.selection_get()
	"""



	#Combo Box
	#comboBoxArmaduras=ttk.Combobox(ventanaArmadura,state='readonly')
	listbox = tk.Listbox(ventanaArmadura,activestyle=tk.NONE,bg="#6C6538",fg="white",width=27)

	#Convertir valoresde las armaduras en letras
	listaTemp=[]
	for i in range(0,len(listaArmadurasPersonales)):
		if(listaArmadurasPersonales[i]==1):
			listaTemp.append("Paolumu Armor")
		elif(listaArmadurasPersonales[i]==2):
			listaTemp.append("Rathalos Armor")
		elif(listaArmadurasPersonales[i]==4):
			listaTemp.append("Nergigante Armor")
		elif(listaArmadurasPersonales[i]==3):
			listaTemp.append("Kushala Daora Armor")
		elif(listaArmadurasPersonales[i]==0):
			listaTemp.append("Sin Armadura")
		else:
			listaTemp.append("Kirin Armor")



	#comboBoxArmaduras['values']=listaTemp
	listbox.insert(0, *listaTemp)
	#comboBoxArmaduras.current(0)
	listbox.selection_set(0)
	#comboBoxArmaduras.grid(row=0,column=0)
	listbox.grid(row=0,column=0)

	botonSeleccionar=Button(ventanaArmadura,text="Seleccione",command=lambda:cambiarImagenArmadura(listbox.selection_get()))
	botonSeleccionar.grid(row=1,column=0)



	
	ventanaArmadura.mainloop()


def mirarInventario():
	ventanaInventario=tk.Toplevel()
	ventanaInventario.title("Monster Hunter")
	ventanaInventario.iconbitmap("rathalos_grande.ico")

	fondo=Label(ventanaInventario)
	imagen=PhotoImage(file="BaulObjetos.png")
	fondo.config(image=imagen)
	fondo.grid(row=0,column=0,rowspan=30,columnspan=30)

	#LLenar Baul
	items=[]
	for i in range(0,len(Inventario)):
		items.append(Inventario[i].getNombre())

	listbox = tk.Listbox(ventanaInventario,activestyle=tk.NONE,bg="#6C6538",fg="white",width=27)
	listbox.grid(row=2,column=27)
	listbox.insert(0, *items)
      
 

	ventanaInventario.mainloop()


def tienda():
	ventanaInventario=tk.Toplevel()
	ventanaInventario.title("Monster Hunter")
	ventanaInventario.iconbitmap("rathalos_grande.ico")

	fondo=Label(ventanaInventario)
	imagen=PhotoImage(file="Forja.png")
	fondo.config(image=imagen)
	fondo.grid(row=0,column=0,rowspan=30,columnspan=30)

	listbox = tk.Listbox(ventanaInventario,activestyle=tk.NONE,bg="#6C6538",fg="white",width=27)
	listbox.grid(row=2,column=27,columnspan=2)
	listbox.insert(0, *listaArmaduras)
	listbox.selection_set(0)

	botonInfo=Button(ventanaInventario,bg="black",fg="white",text="Info Armadura",command=lambda:infoArmadura(listbox))
	botonInfo.grid(row=3,column=27)

	botonSeleccionar=Button(ventanaInventario,bg="black",fg="white",text="Comprar",command=lambda:comprar(listbox))
	botonSeleccionar.grid(row=3,column=28)

	  
 

	ventanaInventario.mainloop()

def infoArmadura(listbox):


	if(listbox.selection_get()=="Nergigante Armor"):
		messagebox.showinfo("Nergigante Armor","Para esta Armadura necesita: Ala de Nergigante y Dosbiscus")
	elif(listbox.selection_get()=="Paolumu Armor"):
		messagebox.showinfo("Paolumu Armor","Para esta armadura necesita: Piel de Paolumu y Hierba Somnifera")
	elif(listbox.selection_get()=="Rathalos Armor"):
		messagebox.showinfo("Rathalos Armor","Para esta armadura necesita: Garra de Rathalos y Hierba de Fuego")
	elif(listbox.selection_get()=="Kushala Daora Armor"):
		messagebox.showinfo("Kushala Daora Armor","Para esta armadura necesita: Escama de Kushala Daora y Hierba de Nieve")
	elif(listbox.selection_get()=="Kirin Armor"):
		messagebox.showinfo("Kirin Armor","Para esta armadura necesita: Cuerno de Kirin y Hierba de Trueno")
	else:
		messagebox.showinfo("Advertencia","No ha seleccionado ninguna armadura")

def ventanaCreador():
	ventana=tk.Toplevel()
	ventana.title("Monster Hunter")
	ventana.iconbitmap("rathalos_grande.ico")

	fondo=Label(ventana)
	imagen=PhotoImage(file="Creator.png")
	fondo.config(image=imagen)
	fondo.grid(row=0,column=0,rowspan=30,columnspan=30)

	labelTitulo=Label(ventana,text="Creador de monstruos",font=("Helvetica",16),fg="white",bg="#84260D")
	labelTitulo.grid(row=0,column=8)

	labelNombre=Label(ventana,text="Nombre: ",fg="white",bg="#84260D",font=("Helvetica", 10))
	labelNombre.grid(row=3,column=0)

	textFieldNombre=Entry(ventana)
	textFieldNombre.grid(row=3,column=1)

	labelDamage=Label(ventana,text="Ataque: ",fg="white",bg="#84260D",font=("Helvetica", 10))
	labelDamage.grid(row=9,column=0)

	spinDamage = Spinbox(ventana, from_=0, to=50,width=4)
	spinDamage.grid(row=9,column=1)

	labelDefense=Label(ventana,text="Defensa: ",fg="white",bg="#84260D",font=("Helvetica", 10))
	labelDefense.grid(row=15,column=0)

	spinDefense= Spinbox(ventana, from_=0, to=50,width=4)
	spinDefense.grid(row=15,column=1)

	botonAceptar=Button(ventana,text="Crear Monstruo",fg="white",bg="black",font=("Helvetica", 12),command=lambda:crearMonstruo(textFieldNombre,spinDamage,spinDefense))
	botonAceptar.grid(row=29,column=8)




	ventana.mainloop()



def ventanaMisionesCompletadas():
	ventana=tk.Toplevel()
	ventana.title("Monster Hunter")
	ventana.iconbitmap("rathalos_grande.ico")

	fondo=Label(ventana)
	imagen=PhotoImage(file="PantallaJuego.png")
	fondo.config(image=imagen)
	fondo.grid(row=0,column=0,rowspan=30,columnspan=30)


	ventana.mainloop()


#-------------------------------Funciones para los Botones------------------------
def pantallaJuegoAbrirNew():
	messagebox.showinfo("Bienvenido Cazador","Bienvenido a Monster Hunter.\nTu objetivo es convertirte en el mejor cazador\n¡Que la estrella azul te acompañe!")
	#Crear archivos para el juego
	nuevaPartida()
	pantallaJuegoAbrir()
	
def pantallaJuegoAbrirLoad():
	messagebox.showinfo("Bienvenido Cazador","Bienvenido de nuevo, recuerda que tiene que cargar cualquier partida\n¡Que la estrella azul te acompañe!")
	cargarPartida()
	#Cargar archivos necesarios
	pantallaJuegoAbrir()

def cambiarImagenArmadura(armor):
	global armorPrincipal

	if(armor==""):
		messagebox.showinfo("Advertencia","No eligio ninguna Armadura")
	else:
		armorPrincipal=armor
		messagebox.showinfo("Armadura","La armadura seleccionada con exito")
	
def Atacar(barraVidaHunter,barraVidaMonstruo,ventana,labelVidaH,labelVidaM,lbPelea):
	global hunter
	global monstruo
	lbPelea.config(text="Se ha avistado un "+monstruo.getNombre())
	monstruo.setVida(hunter.Ataque(monstruo.getVida(),monstruo.getDefense()))
	#time.sleep(0.5)
	hunter.setVida(monstruo.Ataque(hunter.getVida(),hunter.getDefense()))
	labelVidaM.config(text="Vida: "+str(monstruo.getVida()))
	
	if(monstruo.getVida()<=0):
		time.sleep(1)
		lbPelea.config(text="Se ha avistado un "+monstruo.getNombre()+"\nHas atacado, "+monstruo.getNombre()+" ha recibo daño")
		barraVidaMonstruo['value']=monstruo.getVida()
		barraVidaMonstruo.update()
		labelVidaM.config(text="Vida: "+str(monstruo.getVida()))
	else:
		time.sleep(1)
		lbPelea.config(text="Se ha avistado un "+monstruo.getNombre()+"\nHas atacado, "+monstruo.getNombre()+" ha recibo daño.\nEsta apunto de atacar")
		barraVidaMonstruo['value']=monstruo.getVida()
		barraVidaMonstruo.update()
		labelVidaM.config(text="Vida: "+str(monstruo.getVida()))



	if(monstruo.getVida()<=0):
		pass

	else:
		time.sleep(2)
		lbPelea.config(text="Se ha avistado un "+monstruo.getNombre()+"\nHas atacado, "+monstruo.getNombre()+" ha recibo daño.\nEsta apunto de atacar\n"+monstruo.getNombre()+" te ha dado un buen golpe")
		barraVidaHunter['value']=hunter.getVida()
		barraVidaHunter.update()
		labelVidaH.config(text="Vida: "+str(hunter.getVida()))

	

	if(hunter.getVida()<=0):
		labelVidaH.config(text="Vida: "+str(0))
		messagebox.showinfo("Perdio!","Es una mierda  usted!")
		barraVidaMonstruo['value']=100
		barraVidaHunter['value']=100
		monstruo.setVida(100)
		hunter.setVida(100)
		ventana.destroy()


	if(monstruo.getVida()<=0):
		if(monstruo.getNombre()!="Paolumu" and monstruo.getNombre()!="Rathalos" and monstruo.getNombre()!="Kushala Daora" and monstruo.getNombre()!="Nergigante" and monstruo.getNombre()!="Kirin"):
			labelVidaM.config(text="Vida: "+str(0))
			messagebox.showinfo("Felicidades!","Has ganado la partida!\nEres las ostia!")
			barraVidaMonstruo['value']=100
			barraVidaHunter['value']=100
			monstruo.setVida(100)
			hunter.setVida(100)
			ventana.destroy()
		else:
			labelVidaM.config(text="Vida: "+str(0))
			plantaIndice=randint(0, len(listaPlantas)-1)
			materialIndice=0
			#Buscar el material de  monstruo en la lista
			for i in range(0,len(listaMateriales)):
				if(listaMateriales[i].getNombreMonstruo()==monstruo.getNombre()):
					materialIndice=i
					break

			Inventario.append(listaPlantas[plantaIndice])
			Inventario.append(listaMateriales[materialIndice])

			messagebox.showinfo("Felicidades!","Has ganado la partida!\nEres las ostia!\nHas ganado los siguiente objetos: "+listaPlantas[plantaIndice].getNombre()+","+listaMateriales[materialIndice].getNombre()+"\nLos items han sido añadidos a tu Baul")
			barraVidaMonstruo['value']=100
			barraVidaHunter['value']=100
			monstruo.setVida(100)
			hunter.setVida(100)
			ventana.destroy()

def comprar(listbox):

	plantaNecesaria=False
	materialNecesario=False
	tempPlanta=None
	tempMaterial=None
	numeroArmadura=0
	armadura=listbox.curselection()

	for i in range(0,len(Inventario)):
		if(Inventario[i].getTipo()=="Planta"):
			if(listbox.selection_get()=="Paolumu Armor" and Inventario[i].getNombreMonstruo()=="Paolumu"):
				plantaNecesaria=True
				tempPlanta=Inventario[i]
				numeroArmadura=1
				break
			if(listbox.selection_get()=="Rathalos Armor" and Inventario[i].getNombreMonstruo()=="Rathalos"):
				plantaNecesaria=True
				tempPlanta=Inventario[i]
				numeroArmadura=2
				break
			if(listbox.selection_get()=="Kushala Daora Armor" and Inventario[i].getNombreMonstruo()=="Kushala Daora"):
				plantaNecesaria=True
				tempPlanta=Inventario[i]
				numeroArmadura=3
				break
			if(listbox.selection_get()=="Nergigante Armor" and Inventario[i].getNombreMonstruo()=="Nergigante"):
				plantaNecesaria=True
				tempPlanta=Inventario[i]
				numeroArmadura=4
				break
			if(listbox.selection_get()=="Kirin Armor" and Inventario[i].getNombreMonstruo()=="Kirin"):
				plantaNecesaria=True
				tempPlanta=Inventario[i]
				numeroArmadura=5
				break

	for i in range(0,len(Inventario)):
		if(Inventario[i].getTipo()=="Material"):
			if(listbox.selection_get()=="Paolumu Armor" and Inventario[i].getNombreMonstruo()=="Paolumu"):
				materialNecesario=True

				tempMaterial=Inventario[i]
				break
			if(listbox.selection_get()=="Rathalos Armor" and Inventario[i].getNombreMonstruo()=="Rathalos"):
				materialNecesario=True
				tempMaterial=Inventario[i]
				break
			if(listbox.selection_get()=="Kushala Daora Armor" and Inventario[i].getNombreMonstruo()=="Kushala Daora"):
				materialNecesario=True
				tempMaterial=Inventario[i]
				break
			if(listbox.selection_get()=="Nergigante Armor" and Inventario[i].getNombreMonstruo()=="Nergigante"):
				materialNecesario=True
				tempMaterial=Inventario[i]
				break
			if(listbox.selection_get()=="Kirin Armor" and Inventario[i].getNombreMonstruo()=="Kirin"):
				materialNecesario=True
				tempMaterial=Inventario[i]
				break



	
	#plantaNecesaria and materialNecesario

	if(plantaNecesaria and materialNecesario):
		if(numeroArmadura in listaArmadurasPersonales):
			messagebox.showinfo("Advertencia","Esta armadura ya fue comprada!")
		
		else:
			messagebox.showinfo("Armadura","Compra realizada con exito")
			Inventario.remove(tempPlanta)
			Inventario.remove(tempMaterial)
			listaArmadurasPersonales.append(numeroArmadura)

			
				

	else:
		messagebox.showinfo("Advertencia","No cuenta con los materiales necesarios")		

def crearMonstruo(tfNombre,spDamage,spDefense):
	monstruoTemp=Monster(tfNombre.get(),int(spDamage.get()),int(spDefense.get()),100)
	listaMonstruos.append(monstruoTemp)

	messagebox.showinfo("Creador","El monstruo ha sido creado con exito!")

def actualizarcbMisiones(cbMisiones):
	tempLista=[]
	for i in range(0,len(listaMonstruos)):
		tempLista.append(listaMonstruos[i].getNombre())
	cbMisiones['value']=tempLista
	messagebox.showinfo("Misiones","Misiones actualizadas con exito!")
#------------------------------Funciones de los archivos---------------------------

def cargarPartida():

	global listaArmaduras,listaMonstruos,Inventario,listaPlantas,listaMateriales,listaArmadurasPersonales

	"""
	cosas que se cargan, 
	Armaduras
	la lista de armaduras personales se guarda como una lista de 0,1,2,3,4,5

	Monstruos
	Se guardan en una lista de monstruos

	Misiones completadas
	Se guardan en una lista de misiones completadas



	"""

	#Armaduras
	listaArchivoArmaduras=[0,1,2,3,4,5]

	#listaArmaduras.append("Sin Armadura")

	listaArmadurasPersonales=[0,1,2,3,4,5]

	

	listaArmaduras=["Paolumu Armor","Rathalos Armor","Kushala Daora Armor","Nergigante Armor","Kirin Armor"]


	#Monstruos
	rathalos=Monster("Rathalos",10,5,100)
	paolumu=Monster("Paolumu",5,0,100)
	nergigante=Monster("Nergigante",20,15,100)
	kushala=Monster("Kushala Daora",15,10,100)
	kirin=Monster("Kirin",25,20,100)
	listaMonstruos=[paolumu,rathalos,kushala,nergigante,kirin]

	#LLenar inventario
	
	#plantaso
	hierbasom=Item("Hierba Somnifera","Paolumu","Planta")
	hierbafire=Item("Hierba de Fuego","Rathalos","Planta")
	hierbacold=Item("Hierba de Nieve","Kushala Daora","Planta")
	dosbiscus=Item("Dosbiscus","Nergigante","Planta")
	hierbathunder=Item("Hierba de Trueno","Kirin","Planta")
	#Materiales
	pielPaolumu=Item("Piel de Paolumu","Paolumu","Material")
	garraRathalos=Item("Garra de Rathalos","Rathalos","Material")
	escamaKushala=Item("Escama de Kushala Daora","Kushala Daora","Material")
	alaNergigante=Item("Ala de Nergigante","Nergigante","Material")
	cuernoKirin=Item("Cuerno de Kirin","Kirin","Material")

	InventarioArchivo=[hierbasom,hierbafire,hierbacold,dosbiscus,hierbathunder,pielPaolumu,garraRathalos,escamaKushala,alaNergigante,cuernoKirin]

	for i in range(0,len(InventarioArchivo)):
		if(InventarioArchivo[i].getTipo()=="Material"):
			listaMateriales.append(InventarioArchivo[i])
		else:
			listaPlantas.append(InventarioArchivo[i])

def nuevaPartida():
	global listaArmaduras,listaMonstruos,Inventario,listaPlantas,listaMateriales,hunter

	#Llenar al hunter
	#ventanaNombre()



	listaArmaduras=["Paolumu Armor","Rathalos Armor","Kushala Daora Armor","Nergigante Armor","Kirin Armor"]
	listaArmadurasPersonales.append(0)

	#Monstruos
	rathalos=Monster("Rathalos",10,5,100)
	paolumu=Monster("Paolumu",5,0,100)
	nergigante=Monster("Nergigante",20,15,100)
	kushala=Monster("Kushala Daora",15,10,100)
	kirin=Monster("Kirin",25,20,100)
	listaMonstruos=[paolumu,rathalos,kushala,nergigante,kirin]

	#LLenar inventario
	
	#plantas
	hierbasom=Item("Hierba Somnifera","Paolumu","Planta")
	hierbafire=Item("Hierba de Fuego","Rathalos","Planta")
	hierbacold=Item("Hierba de Nieve","Kushala Daora","Planta")
	dosbiscus=Item("Dosbiscus","Nergigante","Planta")
	hierbathunder=Item("Hierba de Trueno","Kirin","Planta")
	#Materiales
	pielPaolumu=Item("Piel de Paolumu","Paolumu","Material")
	garraRathalos=Item("Garra de Rathalos","Rathalos","Material")
	escamaKushala=Item("Escama de Kushala Daora","Kushala Daora","Material")
	alaNergigante=Item("Ala de Nergigante","Nergigante","Material")
	cuernoKirin=Item("Cuerno de Kirin","Kirin","Material")

	InventarioArchivo=[hierbasom,hierbafire,hierbacold,dosbiscus,hierbathunder,pielPaolumu,garraRathalos,escamaKushala,alaNergigante,cuernoKirin]

	for i in range(0,len(InventarioArchivo)):
		if(InventarioArchivo[i].getTipo()=="Material"):
			listaMateriales.append(InventarioArchivo[i])
		else:
			listaPlantas.append(InventarioArchivo[i])

####			

def abrirArchivo():
	ventana=tk.Toplevel()
	ventana.title("Monster Hunter")
	ventana.iconbitmap("rathalos_grande.ico")

	fondo=Label(ventana)
	imagen=PhotoImage(file="fondoMisiones (Copiar).png")
	fondo.config(image=imagen)
	fondo.grid(row=0,column=0,rowspan=10,columnspan=10)

	"""
	archivo=open("Monstruos.txt","r")
	linea=archivo.read()
	temp=""
	for i in range(0,18):
		temp+=linea[i]

	print(temp)
	



	
	"""
	#import TDAFile
	#TDAFileMonstruos=TDAFile("Monstruos.txt")
	#TDAFileMonstruos.open()
	




	listaboxPartidas=tk.Listbox(ventana,activestyle=tk.NONE,bg="gray",fg="white",width=56)
	listaboxPartidas.grid(row=6,column=4,columnspan=2)



	ventana.mainloop()

def guardarArchivo():
	#Guardar Monstruos
	horaInsert=time.strftime("%H:%M:%S")
	horaSalida=time.strftime("%H:%M:%S")
	global listaArmadurasPersonales,fecha,horaEntrada
	TDAFileMonstruos=TDAFile("Monstruos.txt")
	TDAFileMonstruos.openFile()

	for i in range(0,len(listaMonstruos)):
		bufferMonstruos=Buffer("MetadataFile.txt",0)
		bufferMonstruos.setActualObject(listaMonstruos[i])
		TDAFileMonstruos.insert(bufferMonstruos)


	TDAFileMonstruos.closeFile()

	#Partidas
	TDAFilePartida=TDAFile("Partidas Guardadas.txt")
	TDAFilePartida.openFile()


	temp=""

	for i in range(0,len(listaArmadurasPersonales)):
		temp+=str(listaArmadurasPersonales[i])


	partida=PartidaGuardada(hunter.getNombre(),"12345",temp)

	bufferPartidas=Buffer("MetadataFile.txt",1)
	bufferPartidas.setActualObject(partida)
	TDAFilePartida.insert()

	TDAFilePartida.closeFile()


	#Bitacora
	TDAFileBitacora=TDAFile("Bitacora.txt")
	TDAFileBitacora.openFile()

	bitacora=Bitacora(hunter.getNombre(),fecha,horaEntrada,horaSalida,horaInsert)

	bufferBitacora=Buffer("MetadataFile",2)
	bufferBitacora.setActualObject(bitacora)

	#Que si ya existe update




	messagebox.showinfo("Guardado","Ha guardado con exito")




	

	


	


#---------------------------Funciones de ventanas------------------------------

def nombreHunter(tfNombre):
	global hunter
	hunter.setNombre(tfNombre.get())
	messagebox.showinfo("Advertencia","Se agrego")
	


#--------------------------Main---------------------------------------

root1=Tk()
root1.config(bg="#0E6655",width=700,height=500)
root1.iconbitmap("rathalos_grande.ico")
root1.title("Monster Hunter")
fondo=Label(root1)
imagen=PhotoImage(file="Fondo.png")
fondo.config(image=imagen)
fondo.grid(row=0,column=0,rowspan=25,columnspan=25)
botonNewGame=Button(root1,text="New Game",bg="black",fg="white",width=30,height=3,command=pantallaJuegoAbrirNew) 
botonNewGame.grid(row=20,column=20)
botonLoadGame=Button(root1,text="Load Game",bg="black",fg="white",width=30,height=3,command=pantallaJuegoAbrirLoad)
botonLoadGame.grid(row=21,column=20)

#String  de las armaduras
armorPrincipal=""
#Armaduras disponibles
listaArmaduras=[]
listaArmadurasPersonales=[]


#monstruo
listaMonstruos=[]

#Escoger mision
misionEscogida=0

#Variables de la vida
hunter=Hunter("",0,0,0)
monstruo=Monster("",0,0,0)

#Bool de no escogio mision
noMision=False

#Inventario
Inventario=[]
listaMateriales=[]
listaPlantas=[]


#nombrePartida,fecha,horaEntrada,horaSalida,horaInsert
horaEntrada=time.strftime("%H:%M:%S")
horaSalida=""
horaInsert=""
fecha=time.strftime("%d/%m/%y") 


root1.mainloop()



	




