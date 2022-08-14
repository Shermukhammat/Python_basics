# 3. Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya 
#yozing

def katta(son0, son1, son2):
	if son0 < son1:
		kotta = son1
	elif son0 > son1:
		kotta = son0
	else:
		kotta = son0

	if kotta < son2:
		javob = son2
	elif kotta > son2:
		javob = kotta
	else:
		javob = kotta

	return javob


while True:
	son0 = int(input('1-son\n>>>'))
	son1 = int(input('2-son\n>>>'))
	son2 = int(input('3-son\n>>>'))

	print(katta(son1, son2, son0))