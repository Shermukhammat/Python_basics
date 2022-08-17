"""
2.Yuqoridagi funksiyani asl ro'yxatni o'zgartirmaydigan va yangi ro'yxat 
qaytaradigan qilib o'zgartiring

"""

def kottaharf(ruyxat):
	"""
	Ushbu funksiya unga berilgan lug'atning ichidagi harbir so'zning
	birinchi harfini bosh harifga o'tkazib beradi!
	Funksiyadan foydalanish uchun unga 1ta ro'yxat argument beriladi. 
	Funksiya sizga natijani lug'at ko'rinishda qaytaradi!
	"""
	natija = []
	for suz in ruyxat:
		if str(type(suz)) == "<class 'str'>":
			natija.append(suz.title())
		else:
			print(f"\n!!! {suz} matin emass\n")
			natija.append(suz)
	
	return natija

royxat = ['salom', 456, 'shake', 'minecraft']

a = kottaharf(royxat)
print(a)
print(royxat)