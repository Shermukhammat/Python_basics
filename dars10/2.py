#2

#2.Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.

cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']

for n in cars :
	if n.lower() != 'gm':
		print(n.title())
	else:
		print(n.upper())