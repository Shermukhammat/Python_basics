#TUR
#v.1.1.1

def son(son):
	"""
	Ushbu funksya bitta parametir uzting va u sizga o'zgaruvchi son yoki
	son emasligini aniqlab beradi. Yani True va False qiymatlarini 
	qaytaradi!
	"""
	if str(type(son)) == "<class 'int'>":
		javob = True
	else:
		javob = False
	return javob

def matin(matin):
	"""
	Ushbu funksya bitta parametir uzting va u sizga o'zgaruvchi matin yoki
	matin emasligini aniqlab beradi. Yani True va False qiymatlarini 
	qaytaradi!
	"""
	if str(type(matin)) == "<class 'str'>":
		javob = True
	else:
		javob = False
	return javob
