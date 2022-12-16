#28 OBJECT ORIENTED PROGRAMMING. KLASS VA OBYEKT


# son = 1 
# matin = "salom"
# print(type(son))
# print(type(matin))

class Talaba:
	def __init__(self, ism, familya, tugilgan_yil):
		self.name = ism
		self.second_name = familya
		self.born_year = tugilgan_yil

	def tanishtir(self):
		return f"Mening ismim {self.name}, tug'lgan yilim {self.born_year}!"

	def get_name(self):
		return self.name

	def get_age(self, year):
		return year - self.born_year

talaba1 = Talaba("Olim", "Olimov", 2001)
talaba2 = Talaba("Hasan", "Olimov", 2002)
talaba3 = Talaba("Akrom", "Olimov", 2003)

# print(talaba1.second_name)
# print(talaba2.second_name)
# print(talaba3.born_year)

print(talaba1.tanishtir())
print(talaba2.get_name())
print(talaba3.get_age(2022))