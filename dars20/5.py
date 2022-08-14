# 5. Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing 
# (tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta 
# musbat sonlar)

def tub(boshla, toxta):
	oraliq = list(range(boshla, toxta))
	tub_sonlar = []


	bol = 0
	for son in oraliq:
		
		while son >= bol:
			bol+=1
			natija = son % bol 
			if natija == 0:
				tub_sonlar.append(natija)
				break
			else:
				print('...')

	return tub_sonlar

boshla = int(input('Boshla:\n>>>'))
toxta = int(input('To\'xta:\n>>>'))

print(tub(boshla, toxta))