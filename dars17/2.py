#2
"""
Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 
7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm, 18-65 gacha 
10000 so'm, 65 dan kattalarga bepul. Shunday while tsikl yozingki, 
dastur foydalanuvchi yoshini so'rasin va chipta narhini chiqarsin. 
Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin (ikkita 
shartni ham tekshiring). Yuqoridagi dasturni turli usullarda yozib 
ko'ring (break, ishora, yoki shart tekshirish)
"""
toxta = True
yosh  = ''
summa = 0
savol = '\nAssalomu alaykum yoshingz nechchida?>>'

while toxta:

	yosh = input(savol)
    
    if yosh != 'exit' or 'quit':
    	yosh2 = int(yosh)
        
    	if yosh2 <= 7 :
		    summa = 2_000
		    print(f"Sizga kirish {summa} so'm!")

	    elif yosh2 <= 18:
		    summa = 3_000
		    print(f"Sizga kirish {summa} so'm!")
	    
	    elif yosh2 <= 65:
		    summa = 10_000
		    print(f"Sizga kirish {summa} so'm!")
	    
	    else:
		    print('Sizga kirish bepul!')
	
	else:
		print('xayir')
		toxta = False

#  		hohlaysizmi = input('Dasturdan chiqshni hohlaysizmi?(ha\\yo\'q)')


	




