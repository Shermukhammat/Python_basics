"""
4.Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib 
ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, 
ba'zilarini esa almashtiring.
"""

sonlar = [152, -68, 56.39, 56]

sonlar[1] = sonlar[1] + 59 # 1 elementga 59 qo'shlsin;
sonlar.insert(1, 777) #1-indeksga 777 soni qo'shlsin;
del sonlar [-1]  #oxirgi element o'chrilsin;

print(sonlar)