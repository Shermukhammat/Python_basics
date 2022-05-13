#4


mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
    'kartoshka', 'olma', 'banan', 'uzum', 'qovun']

savat=[]
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

z = 0
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        print(f"Do'konimizda {mahsulot} bor")
        z+=1
    else:
        print(f"Do'konimizda {mahsulot} yo'q")

if z == 0:
    print("Savatingiz bo'sh")