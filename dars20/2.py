# 2. Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, va 
# mijozlar degan ro'yxatni shakllantiring.Ro'yxatdagi mijozlar haqidagi 
# ma'lumotni konsolga chiqaring.

def userinfo(name, surname, age, date_of_birth, origin, email = '' , number = None):
	"""
	Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, 
	email manzili va telefon raqamini qabul qilib, lug'at ko'rinishida 
	qaytaruvchi funksiya.
	email va number argumentlarini kiritishni ixtiyoriy qiling
	"""
	if email:
		email = 'Nomalum'
	if number:
		number2 = 'Nomalum'
	else:
		number2 = number

	user={
	'ism' : name, 
	'familya' : surname, 
	'yosh' : age, 
	'tugilgan_yil' : date_of_birth, 
	'tugilgan_joy' : origin, 
	'emayil' : email , 
	'raqam' : number2
	}

	return user 

mijozlar = [] # mijozlar ro'yxati
ishora = True # siklni  to'xtatish uchun ishora
n = 0
z = 0

while ishora: 
	n=+1
	ism = input(f'\nIltimos {n}-mijozning ismini kiriting:\n>>>')
	familya = input(f'\nIltimos {n}-mijoz {ism}ning familyasini kiriting:\n>>>')
	yosh = int(input(f'\nIltimos {n}-mijoz {ism}ning yoshini kiriting:\n(!faqat son kiriting!)\n>>>')) 
	tugilgan_yil = int(input(f'\nIltimos {n}-mijoz {ism}ning \ntug\'ilgan yilini kiriting:\n(!faqat son kiriting!)\n>>>'))
	tugilgan_joy = input(f'\nIltimos {n}-mijoz {ism}ning tug\'ilgan joyini kiriting:\n>>>')
	emayil = input(f'\n{n}.{ism}ning emayili:\n>>>')
	raqam = int(input(f'\n{n}.{ism}ning raqami:\n(!FAQAT RAQAM KIRITING!)\n>>>'))
#	parametrlar = [ism, familya, yosh, tugilgan_yil, tugilgan_joy, emayil, raqam]

	mijozlar.append(userinfo(ism, familya, yosh, tugilgan_yil, tugilgan_joy, email=emayil, number=raqam))


	toxta = input("Yana malumot kiritasizmi!?(xa/yo'q)\n>>>")
	if toxta == 'xa' :
		print('...')

	else:

		ishora = False

for mijoz in mijozlar:
	z += 1
	print(z)
	for kalit, qiymat in mijoz.items():
		print(f"{kalit} : {qiymat}.")
print('Dastur toxtadi!')


	



