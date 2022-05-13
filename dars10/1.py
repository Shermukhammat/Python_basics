#1

"""
1.Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan 
ro'yxat tuzing, ro'yxat elementlarining birinchi harfini katta qilib 
konsolga chqaring. GM uchun ikkala harfni katta qiling.
"""

cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']

for n in cars :
	if n.lower() == 'gm':
		print(n.upper())
	else:
		print(n.title())