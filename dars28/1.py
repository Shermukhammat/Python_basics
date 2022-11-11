# 1.Web sahifangiz uchun foydalanuvchi (user) klassini tuzing. 
# Klassning xususiyatlari sifatida odatda ijtimoiy tarmoqlar talab qiladigan ma'lumotlarni 
# kiriting (ism, foydalanuvchi ismi, email, va hokazo)

# 2.Klassga bir nechta metodlar qo'shing, jumladan get_info() metodi foydalanuvchi haqida 
# yig'ilgan ma'lumotlarni chiroyli qilib chiqarsin (masalan: "Foydalanuvchi: alijon1994, ismi: 
# Alijon Valiyev, email: alijon1994@gmail.com).

# 3.Klassdan bir nechta obyektlar yarating va uning xususiyatlari va metodlariga murojat qiling.

class User:
	def __init__(self, ism, login, email, parol):
		self.name = ism
		self.log = login
		self.email = email
		self.pasword = parol
	def get_info(self):
		return f"Foydalanuvchi ismi: {self.name}.\nFoydalanuvchi logini: {self.log}.\nFoydalanuvchi emaili: {self.email}."

foydalanuvchi = User("SHermuhammad", "Moverik", "temirovshermukhammad@gmail.com", 5678)
print(foydalanuvchi.get_info())
