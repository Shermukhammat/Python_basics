# 2. Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, va 
# mijozlar degan ro'yxatni shakllantiring.Ro'yxatdagi mijozlar haqidagi 
# ma'lumotni konsolga chiqaring.

def userinfo(name, surname, age, date_of_birth, origin, email = '' , number = None):
	"""
	Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, 
	email manzili va telefon raqamini qabul qilib, lug'at ko'rinishida 
	qaytaruvchi funksiya.
	email va number argumentlarini kiritishni ixtiyoriy qilidim
		"""

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

users = []

ishora = True

while ishora :
	ism = input('Foydalanuvchi ismi:\n>>')
	familya = input(f'{ism}ning familyasi:\n>>')
	yosh = int(input(f"{ism} necha yoshda? \n>>"))
	tugilgan_yil = int(input(f"{ism} nechanchi yilda tug'ilgan?\n>>"))
	tugilgan_joy = input(f"{ism} qayerda tavallud topgan? \n>>")
	
	print('\nIxtyoriy ma`lumotlar:\n')

	a = input(f"{ism}ning emayilini kirtasizmi ? (xa\\yo'q)\n>>")
	if a == 'xa':
		emayil = input(f"{ism}ning emayili: \n>>")
	else :
		emayil = ''
	

	b = input(f"{ism}ning raqamini kiritasizmi? (xa\\yo'q)\n>>") 
	if b == 'xa':
		raqam = int(input(f"{ism}ning telefo'n raqami: \n>>"))
	else:
		raqam = None

	users.append(userinfo(ism, familya, yosh, tugilgan_yil, tugilgan_joy, email = emayil, number = raqam))

	sura = input('Yana malumot kiritasizmi? (xa\\yo\'q)\n>>')
	if sura == 'xa':
		ishora = True
	else :
		ishora = False

	if ishora :
		print('\n...')
	else:
		break

for user in users :
	print(user)