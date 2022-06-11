# 1. Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni 
# so'rang. Foydalanuvchi stop so'zini yozishi bilan dasturni 
# to'xtating

nomer = 0
kitob = ''
print('"Stop" deb yozsangiz dastur to\'xtaydi:)!')
kitoblar = []

while kitob.lower() != 'stop':
	nomer+=1
	kitob = input(f'\nYaxshi ko\'rgan {nomer}-kitobingiz nomi>>>')
	if kitob.lower() != 'stop':
		kitoblar.append(kitob)

print(f"Siz yaxshi ko'rgan ", end = '')
for kitob in kitoblar:
	nuqta = ','
	if kitob == kitoblar[-1]:
		nuqta = ' '
	else:
		nuqta = ', '
	print(f"'{kitob.title()}'{nuqta}", end='')
print('lar bazamizga yuklandi!')
	
	



