# 2.Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari 
# ro'yxatini ham qo'shing. For tsikli yordamidamuallifning 
# ismi va uning asarlarini konsolga chiqaring.

a_temur = {
    'shaxs' : 'amir temur',
    't_yil' : '1336',
    't_oy' : 'aprel',
    't_sana' : 19,
    't_joy' : 'shaxrisabz',
    'asari' : 'yo\'q'   
    }

m_eshonqulov = {    
    'shaxs' : 'muhammadali eshonqulov',
    't_yil' : '1994',
    't_oy' : 'noyabir',
    't_sana' : 6,
    't_joy' : 'jizzax',
    'asari' : 'yo\'q'
    }

j_rumiy = {    
    'shaxs' : 'jaloliddin rumiy',
    't_yil' : '1207',
    't_oy' : 'sentyabr',
    't_sana' : 30,
    't_joy' : 'Nomalum',
    'asari' : 'Ichingdagi ichingdadur'
    }

a_navoiy = {   
    'shaxs' : "Alisher Navoiy", 
    't_yil' : 1441, 
    't_oy' : 'fevral',
    't_sana' : 9, 
    "t_joy" : "Xirot",
    'asari' : 'Xamsa'
    }

shaxslar = [a_temur, a_navoiy, j_rumiy, m_eshonqulov]

n=0
for shaxs in shaxslar:
	n=n+1
	print(f"{n}. {shaxs['shaxs'].capitalize()}ning asari {shaxs['asari'].capitalize()}.\n")