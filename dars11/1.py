#1

"""
1.Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa 
"Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.
"""

son = int(input('Juft son kiriting: '))

if (son % 2) == 0 :
	print("Rahmat!")
else:
	print(f"{son} soni juft emas")

