print('\n1.Adabiyot (ilm-fan, san\'at, internet) olamidagi 4 ta mashxur shaxlar ')
print('haqidagi ma\'lumotlarni lug\'at ko\'rinishida saqlang. Lug\'atlarni bitta ')
print('ro\'yxatga joylang, va har bir shaxs haqidagi ma\'lumotni konsolga')
print('chiqaring.')


a_temur = {
    'shaxs' : 'amir temur',
    't_yil' : '1336',
    't_oy' : 'aprel',
    't_sana' : 19,
    't_joy' : 'shaxrisabz'   
    }

m_eshonqulov = {    
    'shaxs' : 'muhammadali eshonqulov',
    't_yil' : '1994',
    't_oy' : 'noyabir',
    't_sana' : 6,
    't_joy' : 'jizzax'
    }

j_rumiy = {    
    'shaxs' : 'jaloliddin rumiy',
    't_yil' : '1207',
    't_oy' : 'sentyabr',
    't_sana' : 30,
    't_joy' : None
    }

a_navoiy = {   
    'shaxs' : "Alisher Navoiy", 
    't_yil' : 1441, 
    't_oy' : 'fevral',
    't_sana' : 9, 
    "t_joy" : "Xirot"
    }


shaxslar = [a_temur, a_navoiy, j_rumiy, m_eshonqulov]

for shaxs in shaxslar:
    print('------------------------------------------------------')

    print(f"SHaxs: {shaxs['shaxs']}, tavallud topgan sanasi: "
        f"{shaxs['t_yil']}-yil {shaxs['t_sana']}-{shaxs['t_oy']}"
        f", tug'ulgan joyi {shaxs['t_joy']}")

    print('------------------------------------------------------')


	
