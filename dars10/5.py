#5

"""
5.Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga 
"Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring.
"""

son = int(input('istalgan son kiriting >>>'))

if son < 0:
	print(f"{son} soni musbat")
elif son > 0:
	print(f"{son} soni manfiy")
else:
	print(f"{son} soni 0ga teng")