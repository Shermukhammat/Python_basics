"""
1. Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, 
email manzili va telefon raqamini qabul qilib, lug'at ko'rinishida 
qaytaruvchi funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin. 
Ba'zi argumentlarni kiritishni ixtiyoriy qiling 
(masalan, tel.raqam, el.manzil)
"""

def userinfo(name, surname, age, date_of_birth, origin, email = '' , number = None):
	"""
	Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, 
	email manzili va telefon raqamini qabul qilib, lug'at ko'rinishida 
	qaytaruvchi funksiya.
	email va number argumentlarini kiritishni ixtiyoriy qiling
	"""
	if email:
		#email = 'Nomalum'
	if number:
		#number2 = 'Nomalum'
	else:
		number2 = number

	user={
	'ism' : name, 
	'familya' : surname, 
	'yosh' : age, 
	'tugilgan_yil' : date_of_birth, 
	'tugilgan_joy' : origin, 
	'email' : email, 
	'raqam' : number2
	}

	return user

 
ism = 'SHermuhammad'
familya = 'Temirov' 
yosh = 19 
tugilgan_yil = 2003
tugilgan_joy = 'Qo\'shrabot'
email = 'temirovshermukhammad@gmail.com'
raqam = 998_97_395_40_03

lugat = userinfo(ism, familya, yosh, tugilgan_yil, tugilgan_joy, email = email, number = raqam)

print(type(lugat))

for kalit, qiymat in lugat.items():
	print(f"\n{kalit} : {qiymat}")