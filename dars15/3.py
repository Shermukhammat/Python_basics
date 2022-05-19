#3
"""
Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu 
davlatning poytaxtini konsolga chiqaring. Agar foydalanuvchi 
lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" 
degan xabarni chiqaring.
"""
davlat = input('Istalgan davlat kiriting ___>>>')

davlatlar = {
	'o\'zbekiston' : 'toshkent',
	'qozog\'iston' : 'olmaota',
	'aqsh' : 'vashingto\'ng',
	'rossiya' : 'maskva',
	'turkiya' : 'istambul',
	'germanya' : 'berlin',
	'fransya' : 'parij',
	'britanya' : 'london',
	'yapo\'niya' : 'tokio'
}

if davlat in davlatlar:
	print(f'{davlat}ning poytaxti {davlatlar[davlat]}!')
else:
	print(f'Kechirasiz biznig ma\'lumotlar bazamizdan \'{davlat}\' afsuski topilmadi:(')
