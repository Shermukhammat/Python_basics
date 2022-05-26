#4
"""
Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh 
juftligini kiriting). Foydalanuvchidan 3 ta ovqat buyurtma 
berishni so'rang. Foydalanuvchi kiritgan taomlarni menu bilan 
solishtiring, agar taom menuda bo'lsa narhini ko'rsating, aks 
holda "bizda bunday taom yo'q" degan xabarni chiqaring
"""

menyu = {
	'osh' : 15_000,
	'somsa' : 8_000,
	'kabob' : 12_000,
	'choy' : 12_00,
	'non' : 4_000,
	'manti' : 18_000,
	'sho\'rva'  : 10_000,
	'qo\'virdoq' : 20_000,
	'mastava' : 15_000,
	'sharbat' : 3_000
    }

for n in range(1,4):
	taom = input(f'{n}-taom nomini kiriting_>>>')
	taom.lower()
	if taom in menyu:
		print(f'{taom.capitalize()}ning narxi {menyu[taom]} so\'m \n')
	else:
		print(f'Bizda {taom} afsuski yo\'q :( \n')


