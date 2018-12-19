#Clase Monster
from Personaje import Personaje
class Monster(Personaje):
	


#------------------------Funciones de Ataque------------------------
	def AtaqueEspecial(self,vidaHunter,defenseHunter):
		damageTemp=self._damage*2 - defenseHunter
		
		vidaHunter=vidaHunter-damageTemp
		return vidaHunter

	def Ataque(self,vidaCazador,defenseHunter):
		damageTemp= self._damage+10 - defenseHunter

		vidaCazador=vidaCazador-damageTemp
		return vidaCazador


	
#Fin clase


