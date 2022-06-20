# 2. Foydalanuvchidan son olib, uning kvadrati va kubini konsolga 
# chiqaruvchi funksiya yozing.

def kvadkub(son333):
	""" Istalgan butun sonni kvadratini va kubni konsolga chiqaruvchi
	funksya. """
	print(f"{son333} ning kvadrati {son333*son333} ga, kubi esa {son333*son333*son333} ga teng!")

while True:
	son = int(input('Istalgan son kiriting:\n>>>'))
	kvadkub(son)
