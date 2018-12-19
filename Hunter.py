#Clase Cazador
from Personaje import Personaje
class Hunter(Personaje):

	#---------Metodos ataque---------------------
	def Ataque(self,vidaMonstruo,defenseMonstruo):
		vidaMonstruo=vidaMonstruo-(self._damage-defenseMonstruo)
		return vidaMonstruo

	def tomarPocion(self):
		self._vida+=20

	