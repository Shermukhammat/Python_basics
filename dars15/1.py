#1
"""
Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z 
qo'shing. Lug'atdagi har bir kalit va qiymatni for tsikli 
yordamida, alifbo ketma-ketligida chiroyli qilib 
konsolga chiqaring.
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

for kalit, qiymat in python_words.items():
	print(f"{kalit}:  \n {qiymat}.")
