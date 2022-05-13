#3

"""
3.10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir 
elementining kubini yangi qatordan konsolga chiqaring.
"""

toq_sonlar = []

for son in range(11, 100, 2):
	toq_sonlar.append(son)

ss = 0

for n in toq_sonlar[:]:
	ss+=1
	print('--------------------')
	print(f"{ss}.  {n}ni kubi {n**3} ga teng.")
	print('--------------------')