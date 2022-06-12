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
savol = 'yosh:'
chiqsh_savoli = 'Dasturdan chiqishni xoxlaysizmi(xa\\yo\'q)?\n>>>'
ishora = True
yosh = 0

while ishora:
    qiymat = input(savol)
    tip = type(qiymat)
    if qiymat == 'exit' or qiymat == 'quit':
        xa_yoq = input(chiqsh_savoli) 
        if xa_yoq.lower() == 'xa':
            ishora = False
            print('...')
        else:
            print('....')
            continue
    # if tip == "<class 'str'>":
    #     print('....')
    #     continue

    else:
        yosh = int(qiymat)
        if yosh <= 7 :
            narx = 2_000
            print(f"Sizga kirish {narx} so'm!")
        elif yosh <= 18:
            narx = 3_000
            print(f"Sizga kirish {narx} so'm!")
        elif yosh <= 65:
            narx = 10_000
            print(f"Sizga kirish {narx} so'm!")
        else:
            narx = 0
            print('Sizga kirish bepul!')