#6

"""
6.foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. 
Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni 
foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. Agar ro'yxatda bunday 
login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda "Xush kelibsiz, 
foydalanuvchi!" xabarini chiqaring.
"""

foydalanuvchlar = ['leon', 'bond', 'bond007', 'shake', 'shake007']

login = 'login'

while True:
	login = input('Iltimos o\'zingizga yangi login kriting _>>>')
	if login in foydalanuvchlar:
		print('---------------------------------------------')
		print(f"'{login}'bu nom band, yangi login tanlang!")
		print('---------------------------------------------')
	else:
		print('---------------------------------------------')
		print("Xush kelibsiz, foydalanuvchi!")
		print('---------------------------------------------')
		break
