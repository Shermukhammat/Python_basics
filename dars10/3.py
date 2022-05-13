#3

"""
3.Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, 
"Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" 
xabarini konsolga chiqaring. Aks holda, "Xushkelibsiz, {foydalanuvchi_ismi}!" 
matnini konsolga chiqaring.
"""

foydalanuvchi_ismi = input('Ismingizni kiriting __>>>')
foydalanuvchi_login = input('Loginingizni kiriting __>>>')

if foydalanuvchi_login.lower() == 'admin':
	print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
	print(f"Xushkelibsiz, {foydalanuvchi_ismi}!")