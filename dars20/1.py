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
	email va number argumentlarini kiritishni ixtiyoriy qilidim
	"""
	
	# elif:
	# 	number2 = number

	user={
	'ism' : name, 
	'familya' : surname, 
	'yosh' : age, 
	'tugilgan_yil' : date_of_birth, 
	'tugilgan_joy' : origin, 
	'email' : email, 
	'raqam' : number
	}
	if email:
		email = 'Nomalum'
	if number:
		number = 'Nomalum'

	return user

 


lugat = userinfo('SHermuhammad', "Temirov", 19, 2003, 'Qo\'shrabot', email = 'temirovshermukhammad@gmail.com', number = 998_97_395_40_00)


for kalit, qiymat in lugat.items():
	print(f"\n{kalit} : {qiymat}")