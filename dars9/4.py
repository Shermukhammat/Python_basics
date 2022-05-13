#4

"""
4.Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar 
degan ro'yxatga saqlab oling.Natijani konsolga chiqaring.
"""

kinolar = []

print('5 ta eng sevimli kinoyingiz nomi?')
for n in range(1, 6):
	kino = input(f"{n}-kino:")
	kinolar.append(kino)

print(kinolar)