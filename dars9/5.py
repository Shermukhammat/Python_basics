#5

"""
5.Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, 
va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. 
Ro'yxatni konsolga chiqaring
"""

people = []

print('Bugun nechta odam bilan suhbatlashdingiz?')
son = int(input('_>_>_>'))
son += 1

for n in range(1, son):
	person = input(f"{n}-odam:")
	people.append(person)

print(people)