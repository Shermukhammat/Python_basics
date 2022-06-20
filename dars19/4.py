# 4. Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi 
# funksiya yozing. Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni 
# chiqaring.

def qaysi_katta(aa = 0, bb = 0):
	"""Ikkita parametirdan qaysi biri kattaligini aniqlovchi funksya. """
	if aa == bb :
		print(f"{aa} va {bb} o'zaro teng!")
	elif aa > bb :
		print(f"{aa} soni {bb} dan katta!")
	else:
		print(f"{bb} soni {aa} dan katta!")

son0 = int(input("\nson1:\n>>>"))
son1 = int(input("\nson2:\n>>>"))

qaysi_katta(son0, son1)