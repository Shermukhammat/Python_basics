kk'k'j]j'j''jkl]j';
'
k\vl# 5. Foydalanuvchidan x va y sonlarini olib, x^y ni konsolga chiqaruvchi 
# funksiya yozing.Yuqoridagi funksiyada y uchun 2 standart qiymatini bering.

def daraja(son = 0, darajasi = 0) :
	""" 
	foydalanuvchidan son va daraja parametirlarini olib natijani
	hisoblab konsolga chiqaruvchi funksya!
	"""
	natija = son**darajasi
	print(f"\n{son} ^ {darajasi} = {natija}")

son = int(input('\nsonni kiriting:\n>>>'))
son_darajasi = int(input(f'\n{son} ni darajasini kiriting:\n>>>'))

daraja(son = son, darajasi = son_darajasi)