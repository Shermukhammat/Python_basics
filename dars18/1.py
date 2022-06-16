# 1. Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. 
# Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.

mahsulotlar = []
n = 1 #Mahsulot tartib raqami uchun o'zgaruvchi.
print(f"\nIltimos harid qilmoqchi bo'lgan mahsulotlaringiz nomini kiriting!\n")

while True:
	mahsulot = input(f"\n{n}-mahsulot nomi:\n>>>")
	n+=1
	mahsulotlar.append(mahsulot)
	ishora = input("Yana mahsulot nomini kirtasizmi(ha\\yo'q)!?")

	if ishora.lower() != 'ha':
		break
n = 0
for mahsulot in mahsulotlar:
	n+=1
	print(f"\n{n}-mahsulot: '{mahsulot}'")

