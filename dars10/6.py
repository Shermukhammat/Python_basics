#6

"""
6.Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa 
uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, 
"Musbat son kiriting" degan xabarni chiqaring.
"""
while True:
	son = input('son kiriting _>>>')
	if not son.isnumeric():
		continue
	son = int(son)
	if son >= 0:
		print(f"{son}ning ildzi  {son**(1/2)}ga teng!")
		break
	else:
		print("Musbat son kiriting")
