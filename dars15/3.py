#3
"""
Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu 
davlatning poytaxtini konsolga chiqaring. Agar foydalanuvchi 
lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" 
degan xabarni chiqaring.
"""


davlatlar = {
	'O\'zbekiston' : 'Toshkent',
	'Qozog\'iston' : 'Olmaota',
	'AQSH' : 'Vashingto\'ng',
	'Rossiya' : 'Maskva',
	'Turkiya' : 'Istambul',
	'Germanya' : 'Berlin',
	'Fransya' : 'Parij',
	'Britanya' : 'London',
	'Yapo\'niya' : 'To\'kio'
    }

kirish = input('Istalgan davlat kiriting ___>>>')

if kirish.lower() == 'aqsh':      #agar kirish aqsh bolsa;
	davlat = kirish.upper()       #davlat = kirish yuqori registir bn yozilganiga;
else:                             #aks holda;
	davlat = kirish.capitalize()  #davlat = kirishning 1-harfi yuqori registor bilan yozilganiga;

if davlat in davlatlar:
	
	print(f'{davlat}ning poytaxti {davlatlar[davlat]}!')
else:
	print(f'Kechirasiz biznig ma\'lumotlar bazamizdan \'{davlat}\' afsuski topilmadi:(')
