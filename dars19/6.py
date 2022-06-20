# 6. Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan 
# sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya yozing. 
# Natijalarni konsolga chiqaring. 


def qoldiqsiz(son ,boshla = 2, toxta = 11):
	"""
	ushbu funksya berilgan qiymatni n dan m gacha bo'lgan sosonlarga 
	qoldiqsiz bo'lnshini yoki bo'linmashligini aniqlab beradi!.
	n buyerda boshla atributi m esa toxta atributlaridir!
	standar bo'ycha boshla = 2 ga toxta esa = 11 ga.
	"""
	for n in range(boshla, toxta):
		if son % n == 0 :
			print(f"\n{son} soni {n} ga qoldiqsiz bo'linadi!")
		else:
			print(f"\n{son} soni {n} ga qoldiqsiz bo'linmaydi!")

qoldiqsiz(100)