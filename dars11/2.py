#2

"""
2.Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha 
chiqaring:
Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm
"""

yosh = int(input('Yoshingiz nechida _>_>_>'))

if yosh <= 4 :
	print(f"Sizga kirish bepul!")
elif yosh >= 60:
	print(f"Sizga kirish bepul!")
elif yosh <= 18:
	print('Sizga chipta  narxi 10 000 so\'m!')
else:
	print('Sizga chipta  narxi 20 000 so\'m!')