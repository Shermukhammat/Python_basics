# 5.Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha 
# davlatlarni emas, foydalanuvchi so'ragan davlat haqida ma'lumot 
# bering. Agar davlat sizning lug'atingizda mavjud bo'lmasa, "Bizda 
# bu davlat haqida ma'lumot yo'q" degan xabarni chiqaring.


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


    'aqsh' : {
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

axborot = input('Davlat nomini kiriting>>>')
if axborot.lower() in davlatlar.keys():
    chiqar = davlatlar[axborot.lower()]
    print(f"\n{axborot.title()}ning poytaxti {chiqar['poytaxti']}")
    print(f"Maydoni {chiqar['maydoni']} km2.") 
    print(f"Axolisi esa {chiqar['axolisi']} kishi.")
    print(f"Pul birlig '{chiqar['puli']}'.\n\n")
else:
    print(f"{axborot.title()}ni malumotlar bazamizdan topa olmadik!")
