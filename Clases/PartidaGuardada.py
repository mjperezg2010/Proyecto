# Clase partida  guardada
class PartidaGuardada():

	def __init__(self,nombrePartida,misionesCompletadas):

	#misiones completadas es una lista del 1 al 5, porque son 5 misiones
		self.__misionesCompletadas=misionesCompletadas
		self.__nombrePartida=nombrePartida


	#------------------------Set and Gets----------------------

	def setNombrePartida(self,nombrePartida):
		self.__nombrePartida=nombrePartida

	def getNombrePartida():
		return self.__nombrePartida

	def setMisionesCompletadas(self,misionesCompletadas):
		self.__misionesCompletadas=misionesCompletadas

	def getMisionesCompletadas(self):
		return self.__misionesCompletadas