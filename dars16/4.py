# 4.Davlatlar degan lug'at yarating, lug'at ichida bir nechta 
# davlatlar haqida ma'lumotlarni lug'at ko'rinishida saqlang. 
# Har bir davlat haqida ma'lumotni konsolga chiqaring.

davlatlar = {

    'o\'zbekiston' : {
        'poytaxti' : 'Toshkent',
        'maydoni' : 447_400,
        'puli' : 'so\'m',
        'axolisi' : 35_445_000 },#2022-yil hsobi b.n.

    'rossiya' : {
        'poytaxti' : 'Moskva',
        'maydoni' : 17_100_000,
        'puli' : 'rubil',
        'axolisi' : 145_300_000 },#2002-yil hsobi b.n.


    'AQSH' : {
        'poytaxti' : 'Vashingtong',
        'maydoni' : 9_800_000,
        'puli' : 'dollor',
        'axolisi' : 331_000_000 },#2022-yil hsobi b.n.
 

    'germanya' : {
        'd_nomi' : 'Germanya',
        'poytaxti' : 'Berlin',
        'maydoni' : 357_000,
        'puli' : 'marka',
        'axolisi' : 83_149_300  },#2019-yil hsobi b.n.
    

    'turkiya' : {
        'poytaxti' : 'Istanbul',
        'maydoni' : 783_562,
        'puli' : 'Lira',
        'axolisi' : 84_680_273 #2021-yil hsobi b.n.
    }
}

for davlat, malumot in davlatlar.items():
    print(f"{davlat.title()} davlatining poytaxti {malumot['poytaxti']}.")
    print(f"Maydoni {malumot['maydoni']} km2.") 
    print(f"Axolisi esa {malumot['axolisi']} kishi.")
    print(f"Pul birlig '{malumot['puli']}'.\n\n")
