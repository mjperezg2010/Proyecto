# Clase partida  guardada
class PartidaGuardada():

	def __init__(self,nombrePartida,misionesCompletadas,armadurasObtenidas):

	#misiones completadas es una lista del 1 al 5, porque son 5 misiones
		self.__misionesCompletadas=misionesCompletadas
		self.__nombrePartida=nombrePartida
		self.__armadurasObtenidas=armadurasObtenidas


	#------------------------Set and Gets----------------------

	def setNombrePartida(self,nombrePartida):
		self.__nombrePartida=nombrePartida

	def getNombrePartida(self):
		return self.__nombrePartida

	def setMisionesCompletadas(self,misionesCompletadas):
		self.__misionesCompletadas=misionesCompletadas

	def getMisionesCompletadas(self):
		return self.__misionesCompletadas

	def setArmadurasObtenidas(self,armadurasObtenidas):
		self.__armadurasObtenidas=armadurasObtenidas

	def getArmadurasObtenidas(self):
		return self.__armadurasObtenidas

	def getKey(self):
		return self.__nombrePartida