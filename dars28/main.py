#28

class Talaba:
	def __init__(self, ism, familya, tyil):
		self.name = ism
		self.familya = familya
		self.tyil = tyil
	def tanishtir(self):
		return f"Ismim {self.name} familyam {self.familya}"
	def get_name(self):
		return self.name
	def get_age(self, yil):
		return yil - self.tyil
	def get_lastname(self):
		return self.familya
talaba1 = Talaba("Olim", "Olimov", 2000)
talaba2 = Talaba("Hasan", "hasanov", 2007)
talaba3 = Talaba("Ali", "Alimov", 2008)
print(talaba1.tanishtir())
print(talaba1.tyil)
print(talaba1.get_name())
print(talaba3.get_age(2022))
print(talaba1.get_lastname())


