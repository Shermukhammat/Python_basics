#28-dars vazifa

"""
1.Web sahifangiz uchun foydalanuvchi (user) klassini tuzing. Klassning xususiyatlari sifatida 
odatda ijtimoiy tarmoqlar talab qiladigan ma'lumotlarni kiriting (ism, foydalanuvchi ismi, 
email, va hokazo)

2.Klassga bir nechta metodlar qo'shing, jumladan get_info() metodi foydalanuvchi 
haqida yig'ilgan ma'lumotlarni chiroyli qilib chiqarsin (masalan: "Foydalanuvchi: 
alijon1994, ismi: Alijon Valiyev, email: alijon1994@gmail.com).

3.Klassdan bir nechta obyektlar yarating va uning xususiyatlari va metodlariga murojat 
qiling.

"""

#1
class User:
	def __init__(self, ism, familya, login, parol, age, mamlakat):
		self.name = ism
		self.surname = familya
		self.login = login
		self.cod = parol
		self.age = age
		self.region = mamlakat

	def get_info(self):
		"""Foydalanuvchi haqidagi malumotlarni qaytaradi."""
		return f"\nFoydalanuvchi ism familyasi {self.surname} {self.name},\nyoshi {self.age} da,\nLogini: <{self.login}>, \nparoli: <{self.cod}> \nMamlakat: <{self.region}>.\n"

	def get_age(self):
		"""Foydalanuvchi yoshni qaytaradi. """
		return self.age

	def get_born_year(self, year):
		"""Tug'lgan yilni qaytaradi. """
		return year - self.age 

	def get_name(self):
		"""Foydalanuvchi ismni qytaradi. """
		return self.name

	def get_surname(self):
		"""Foydalanuvchi familyasini qaytaradi. """
		return self.surname





foydalanuvchi1 = User("SHermuhammad", "Temirov", "agent_007", 12345, 19, "O'zbekiston")

print(foydalanuvchi1.get_born_year(2022))