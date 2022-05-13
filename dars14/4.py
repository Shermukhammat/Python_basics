#4
"""
Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini 
yuqoridagi lug'atdan chiqarib bering. Agar so'z lu'gatda mavjud bo'lmasa, 
"Bunda so'z mavjud emas" degan xabarni chiqaring.
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
	'if' : 'agar shart  operatori',
	'elif' : 'aksholda shart operatori',
	'for' : 'uchun takrorlanish opertori',
	'int()' : 'malumotni int malumot turiga otkazuvchi funksya',
	'str()' : 'malumotni str malumot turiga otkazuvchi funksya',
	'input()' : 'foydalanuvchidan malumot sorovchi funksya'
	}



axborot = input('iltimos python atamasi kriting_>>>')
chopet = python_words.get(axborot, f'Afsuski {axborot} topilmadi :(')
print(chopet)


