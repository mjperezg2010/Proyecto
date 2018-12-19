#Clase Personaje

class Personaje():

	def __init__(self,nombre, damage, defense, vida):
		self._nombre=nombre
		self._damage=damage
		self._defense=defense
		self._vida=vida


	#-------------------Sets and gets------------------------
	def setNombre(self,nombre):
		self._nombre=nombre

	def getNombre(self):
		return self._nombre

	def setDamage(self,damage):
		self._damage=damage

	def getDamage(self):
		return self._damage

	def setDefense(self,defense):
		self._defense=defense

	def getDefense(self):
		return self._defense

	def setVida(self,vida):
		self._vida=vida

	def getVida(self):
		return self._vida

