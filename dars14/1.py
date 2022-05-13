#1
"""
otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga 
shu inson haqida kamida 3 ta m'alumot kiriting (ismi, tu'gilgan yili, 
shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida konsolga 
chiqaring: 
Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan
"""

otam = {
    'azo' : "ota",
    'ism' : 'xolboy',
    't_yil' : 1956,
    't_viloyat' : 'samarqand'
	}

onam = {
    'azo' : 'ona',
    'ism' : 'gulnora',
    't_yil' : 1956,
    't_viloyat' : 'samarqand'
	}

akam = {
    'azo' : 'aka',
    'ism' : 'ro\'ziboy',
    't_yil' : 1994,
    't_viloyat' : 'samarqand'
	}


oyla_azolari = [otam, onam,akam]
for azo in oyla_azolari:
	print(f"{azo['azo'].title()}ning ismi {azo['ism'].title()} {azo['t_yil']}-yili {azo['t_viloyat'].title()} viloyatida tug\'ilgan")

