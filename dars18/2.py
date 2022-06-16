# 2. e-bozor uchun mahsulotlar va ularning narhlari lug'atini 
# shakllantiruvchi dastur yozing. Foydalanuvchidan lug'atga bir nechta 
# elementlar (mahsulot va uning narhi) kiritishni so'rang.

mahsulotlar = {}
n = 1 #mahsulot tartib raqami uchun o'zgaruvchi!
print("\nIltimos e-bozor uchun mahsulotlar haqida malumotlar kiriting!")

while True:
	mahsulot_nomi = input(f"\n{n}-mahsulot nomi:\n>>>")
	mahsulot_narxi = input(f"\n'{mahsulot_nomi}'ning narix necha so'm( faqat raqam kiriting!)!?\n>>>")
	ishora = input('Yana malumot kiritasizmi(ha\\yo\'q)!?\n>>>')
	n+=1

	mahsulotlar[mahsulot_nomi] = int(mahsulot_narxi)

	if ishora.lower() != 'ha':
		print('...')
		break

n = 0
for kalit, qiymat in mahsulotlar.items():
	n+=1
	print(f"{n}-mahsulot: '{kalit}'. Narxi : {qiymat} so'm")

