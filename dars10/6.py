#6

"""
6.Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa 
uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, 
"Musbat son kiriting" degan xabarni chiqaring.
"""

son = int(input('istalgan son kiriting _>>>'))
if son >= 0:
	print(f"{son}ning ildzi  {son**(1/2)}ga teng!")
else:
	print("Musbat son kiriting")