#5

"""
5.Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 
ta mahsulot kiritishni so'rang.Foydalanuvchi so'ragan va do'konda bor mahsulotlarni 
yang, bor_mahsulotlar degan ro'yxatga, do'konda yo'q mahsulotlarni esa mavjud_emas 
degan ro'yxatga qo'shing. Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha 
mahsulotlar do'konimizda bor" degan xabarni, aks holda esa "Quyidagi mahsulotlar
do'konimizda yo'q: ....." degan xabarni chiqaring.
"""

mahsulotlar = ['olma', 'banan', 'anor', 'xurmo', 'olcha', 
    'pepsi', 'muzqaymoq', 'guruch', 'shokolad', 'fanta' 
    
    ]


savat = []
bor_mahsulotlar = []
mavjud_emas = []
anqlovchi = 0

for n in range(1, 6):
	z = input(f"{n}-mahsulotni kiriting:")
	savat.append(z)

for mahsulot in savat:
	if mahsulot in mahsulotlar:
		bor_mahsulotlar.append(mahsulot)
	else:
		anqlovchi+=1
		mavjud_emas.append(mahsulot)

if anqlovchi == 0:
	print('Siz so\'ragan barcha mahsulotlar do\'konimzda bor')
else:
	print("Siz so'ragan do'konimzda mavjud mahsulotlar: ")
	for n in bor_mahsulotlar:
		print('---------------------')
		print(n)
	    print('---------------------')
	    
	print("Siz so'ragan do'konimzda mavjud bo'lmagan mahsulotlar: ")
	for n in mavjud_emas:
	    print('---------------------')
    	print(n)
        print('---------------------')

    
    
    
    	
