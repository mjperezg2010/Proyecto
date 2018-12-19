#Bitacora

class Bitacora():

	def __init__(self,nombrePartida,fecha,horaEntrada,horaSalida,horaInsert):
		self.__nombrePartida=nombrePartida
		self.__fecha=fecha
		self.__horaEntrada=horaEntrada
		self.__horaSalida=horaSalida
		self.__horaInsert=horaInsert

	#-----------------------Sets and Gets---------------------------

	def setNombrePartida(self,nombrePartida):
		self.__nombrePartida=nombrePartida

	def getNombrePartida(self):
		return self.__nombrePartida

	def setFecha(self,fecha):
		self.__fecha=fecha

	def getFecha(self):
		return self.__fecha

	def setHoraEntrada(self,horaEntrada):
		self.__horaEntrada=horaEntrada

	def getHoraEntrada(self,):
		return self.__horaEntrada

	def setHoraSalida(self,horaSalida):
		self.__horaSalida=horaSalida

	def getHoraSalida(self):
		return	self.__horaSalida

	def setHoraInsert(self,horaInsert):
		self.__horaInsert=horaInsert

	def getHoraInsert(self):
		return self.__horaInsert

