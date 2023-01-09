class Talaba:
	def __init__(self, ism, familya, tyil):
		self.name = ism
		self.familya = familya
		self.tyil = tyil
		self.bosqich = 1

	def tanishtir(self):
		return f"Ismim {self.name} familyam {self.familya}"

	def get_name(self):
		""" Talabaning ismni qaytaruvchi metid"""
		return self.name

	def get_age(self, yil):
		""" Talabaning yoshni qaytaruvchi metod. yil -> hozirgi yil"""
		return yil - self.tyil

	def get_lastname(self):
		return self.familya

	def get_lable(self):
		return self.bosqich

	def talaba_update(self):
		return self.bosqich


talaba1 = Talaba("SHermuhammad", "Temirov", 2003)
print(talaba1.tanishtir())

class Fan():
	"""
	Fan nomli klas
	"""

	def __init__(self, nom):
		self.nom = nom
		self.talabalar_soni = 0
		self.talabalar = []

	def add_students(self, talaba):
		self.talabalar.append(talaba)
		self.talabalar_soni += 1


# matem = Fan("Matem")
# matem.add_students(talaba1)

# print(matem.nom)
# print(matem.talabalar_soni)
# print(matem.talabalar[0].name)
