# 5. Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing 
# (tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta 
# musbat sonlar)

def tub(boshla, toxta):
	oraliq = list(range(boshla, toxta))
	tub_sonlar = []
	murakkab_sonlar = []
	for son in oraliq:
		ishora = True
		buluvlar = list(range(2, son))
		

		for buluv in buluvlar:
			if son % buluv == 0 :
				ishora = False
			


		if ishora and son != 1:
			tub_sonlar.append(son)

		else:
			murakkab_sonlar.append(son)

	return tub_sonlar







boshla = int(input('Boshla:\n>>>'))
toxta = int(input('To\'xta:\n>>>'))

print(tub(boshla, toxta))