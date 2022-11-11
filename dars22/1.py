 """
1. Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi 
funksiya yozing

"""
from tur import son

def kupayt(*qiymatlar):
	javob = 1
	for qiymat in qiymatlar:
		if son(qiymat):
			javob = javob * qiymat
		else:
			print(f"\n!!! '{qiymat}' son emas !!!\n")

	return javob

print(kupayt(5, 5, 5, 'ola', 'HTML', 55, "AI"))
