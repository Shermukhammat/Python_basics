# 3. Foydalanuvchidan son olib, son juft yoki toqligini konsolga 
#chiqaruvchi funksiya yozing.

def toqjufttop(son333):
	"""Berilgan argumentni toq yoki juftligini aniqlab beruvchi funksya!"""
	if son333 / 2 == 0 :
		print(f"{son333} juft son!")
	else:
		print(f"{son333} toq son!")

print('\n Berilgan sonning juf yoki toq son ekanligini topib beruvchi dastur!\n')
son  =int(input("Istalga son kiriting:\n>>>"))
toqjufttop(son)