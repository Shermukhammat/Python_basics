"""
1.Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir 
matnning birinchi harfini katta harfga o'zgatiruvchi funksiya 
yozing.
"""

#1.Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning 
#birinchi harfini katta harfga o'zgatiruvchi funksiya yozing.

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

print(kottaharf(royxat))