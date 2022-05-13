#2
"""
Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 
5 ta ism-taom jufltigi bo'lsin. Kamida uch kishining sevimli taomini konsolga 
chiqaring: 
Alining sevimli taomi osh
"""

otam = {
    'azo' : "ota",
    'ism' : 'xolboy',
    't_yil' : 1956,
    't_viloyat' : 'samarqand',
    's_taom' : 'osh'
    }

onam = {
    'azo' : 'ona',
    'ism' : 'gulnora',
    't_yil' : 1956,
    't_viloyat' : 'samarqand',
    's_taom' : 'sho\'rva'
	}

akam = {
    'azo' : 'aka',
    'ism' : 'ro\'ziboy',
    't_yil' : 1994,
    't_viloyat' : 'samarqand',
    's_taom' : 'somsa'
	}

oyla_azolari = [otam, onam, akam]

for azo in oyla_azolari:
	print(f"{azo['azo'].title()}mning sevimli taomi {azo['s_taom']}.")