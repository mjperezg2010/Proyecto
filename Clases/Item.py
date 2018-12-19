#Planta

class Item():

	def __init__(self,nombre,nombreMonstruo,tipo):
		self.__nombre=nombre
		self.__nombreMonstruo=nombreMonstruo
		self.__tipo=tipo


	#--------Sets and gets

	def setNombre(self,nombre):
		self.__nombre=nombre

	def getNombre(self):
		return self.__nombre

	def setNombreMonstruo(self,nombreMonstruo):
		self.__nombreMonstruo=nombreMonstruo

	def getNombreMonstruo(self):
		return self.__nombreMonstruo

	def setTipo(self,tipo):
		self.__tipo=tipo

	def getTipo(self):
		return self.__tipo