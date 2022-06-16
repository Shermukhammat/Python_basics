"""
3. Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi 
ro'yxatidagi har bir mahsulotni e-bozordagi mahsulotlar bilan solishitiring 
(tayyor ro'yxat ishlatishingiz mumkin). Agar mahsuot e-bozorda mavjud
bo'lsa mahuslot narhini chiqaring, aks holda "Bizda bu mahsulot yo'q" 
degan xabarni kor'sating.
"""

mahsulotlar = {
	'olma' : 2_000,
	'banan' : 17_000,
	'olcha' : 25_000,
	'pepsi' : 8_000,
	'coca cola' : 8_000,
	'fanta' : 8_000,
	'sut' : 5_000,
	'muzqaymoq' : 4_000,
	'non' : 3_000,
	'baliq' : 6_000,
	'anor' : 12_000,
	'shokalad' : 5_000,
	'margarin' : 10_000
}


n = 1 #Mahsulot tartib raqami uchun o'zgaruvchi.
print(f"\nIltimos harid qilmoqchi bo'lgan mahsulotlaringiz nomini kiriting!\n")
savat = []

while True:
	xarid = input(f"\n{n}-mahsulot nomi:\n>>>")
	savat.append(xarid.lower())
	n+=1
	ishora = input('\nYana mahsulot xarid qilasizmi(xa\\yo\'q)?\n>>>')

	if ishora.lower() != 'xa':
		print('...')
		break

for xarid in savat:
	if xarid in mahsulotlar:
		print(f"\n'{xarid}'' bor narxi: {mahsulotlar[xarid]} so'm.")