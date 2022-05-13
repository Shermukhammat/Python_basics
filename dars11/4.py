#4

"""
4.mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. 
Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 
ta mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati 
bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" 
aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.
"""

mahsulotlar = ['olma', 'banan', 'anor', 'xurmo', 'olcha', 
    'pepsi', 'muzqaymoq', 'guruch', 'shokolad', 'fanta' 
    
    ]


savat = []


for n in range(1, 6):
	z = input(f"{n}-mahsulotni kiriting:")
	savat.append(z)

for mahsulot in savat:
	if mahsulot in mahsulotlar:
		print(f"{mahsulot} do'konimzda bor!")
	else:
		print(f"{mahsulot} do'konimzda afsuski yo'q :(")
	

