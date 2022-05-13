#5
"""
Yuqoridagi matnni f-string yordamida, yangi, manzil deb nomlangan o'zgaruvchiga
yuklang manzilga biz yuqorida o'rgangan title(), upper(), lower() , capitalize() metodlarini
qo'llab ko'ring.
"""


kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor"
viloyat="Samarqand"



manzil = f"Siz {kocha.title()} kochasi, {mahalla.capitalize()} mahallasi, {tuman.upper()} tumani, {viloyat.lower()} viloyatda yashar ekansiz"

print(manzil)