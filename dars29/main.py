class Talaba:
	def __init__(self, ism, familya, tyil):
		self.name = ism
		self.familya = familya
		self.tyil = tyil
		self.bosqich = 1
	def tanishtir(self):
		return f"Ismim {self.name} familyam {self.familya}"
	def get_name(self):
		return self.name
	def get_age(self, yil):
		return yil - self.tyil
	def get_lastname(self):
		return self.familya
	def talaba_update():


# talaba1 = Talaba("SHermuhammad", "Temirov", 2003)
# talaba1.bosqich = 3
# print(talaba1.bosqich)

class Fan():
	"""
	Fan nomli klas
	"""

	def __int__(self, nom):
		self.nom = nom
		self.talabalar_soni = 0
		self.talabalar = []


matem = Fan

