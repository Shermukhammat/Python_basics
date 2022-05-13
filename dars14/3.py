#3
"""
Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta 
so'z (atamani) kiriting (masalan integer, float, string, if, else va hokazo) 
va har birining qisqacha tarjimasini yozing.
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
for word in python_words:
	print('-----------------')
	print(f'{word}: \n{python_words[word]}')
	print('-----------------')

