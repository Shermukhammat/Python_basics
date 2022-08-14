# 4. Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, 
# diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya 
# yozing

def aylana(radiyus):
	"""
	C - Aylana
	D - Diametri
	R - radiyusi
	L - uzunligi
	Y - Yuzi	

	ushbu funksya aylananing radiyusini qabul qilib uning radiusini, 
	diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya
	"""
	PI = 3.14
	R = radiyus
	D = 2*R
	L = 2*PI*R

	javob = {
	'radiyus' : R,
	'diametr' : D,
	'uzunlik' : L
	}

	return javob

print(aylana(10))