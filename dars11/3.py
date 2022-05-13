#3

"""
3.Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning 
teng yoki katta/kichikligi haqida xabarni chiqaring
"""

son1 = int(input('Son1: ')) 

son2 = int(input('Son2: '))

if son1 == son2:
	print(f"{son1} va {son2} sonlari ozaro teng!")
elif son1 > son2:
	print(f"{son1} soni {son2} dan katta!")
else:
	print(f"{son1} soni {son2} dan kichkina!")