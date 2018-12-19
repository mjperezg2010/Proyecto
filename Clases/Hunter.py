#Clase Cazador

class Hunter(Personaje):

	#---------Metodos ataque---------------------
	def Ataque(self,vidaMonstruo,defenseMonstruo):
		vidaMonstruo=vidaMonstruo-(self._ataque-defenseMonstruo)
		return vidaMonstruo

	def tomarPocion(self):
		self._vida+=20

	