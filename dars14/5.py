#5
"""
Yuqoridagi vazifani if-else yordamida qiling va natijani ham foydalanuvchiga 
tushunarli ko'rinishda chiqaring.
"""

python_words = {
	'int' : 'Integer raqamli (butun son) malumot turi. ',
	'float' : 'butun son malumot turi',
	'str' : 'yozuvli malumot turi',
	'dict' : 'Lug\'at (dictionary) malumot turi',
	'bool' : 'mantiqy (boolen) malumot turi',
	'list' : 'Ro\'yhat (list) malumot turi',
	'print()' : 'malumotlarni chiqaruvchi funksya',
	'type()' : 'malumot turini aniqlab beruvchi funksya',
	'if' : 'agar deb nomlanuvchi shart  operatori',
	'elif' : 'aksholda shart operatori',
	'for' : 'uchun takrorlanish opertori',
	'int()' : 'malumotni int malumot turiga otkazuvchi funksya',
	'str()' : 'malumotni str malumot turiga otkazuvchi funksya',
	'input()' : 'foydalanuvchidan malumot sorovchi funksya'
	}



axborot = input('pythonga oid atam kriting:')

javob = python_words.get(axborot)

if javob.lower == 'none':
	print(f'{axborot} topilmadi!')
else:
	print(javob)