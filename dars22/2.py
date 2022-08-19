"""
2. Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi 
funkisya yozing. Talabaning ismi va familiyasi majburiy argument, qolgan 
ma'lumotlar esa ixtiyoriy ko'rinishda istalgancha berilishi mumkin
bo'lsin.
"""

def talaba(ism, familya, **malumot):
	malumot['ism'] = ism
	malumot['familya'] = familya
	return malumot

saqla = talaba('SHermuhammad', 'Temirov', yoshi = 19, viloyat = 'samarqand')

print(saqla)