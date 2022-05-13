#17.Yuqoridagi nonishta  ro'yhatini o'zgarmas
#ro'yhatga  aylantiring va nonushta[0] = "qaymoq
#va non" deb qiymat berib ko'ring.


taomlar = ['osh', 'manti', 'sho\'rva', 'somsa', 'kabob']

nonushta = taomlar[:]

#print(f"nonushta ro'yxati: {nonushta}")

nonushta.remove('osh')
del nonushta[0]
nonushta.append('CHoy')
nonushta.insert(0, 'Sut')


nonushta = tuple(nonushta) #noushta ro'yxatini o'zgarmas ro'yxatga aylantirdim
print(type(nonushta))

nonushta[0] = "qaymoq va non" # Baribir xatolik beradi!
print(f"nonushta ro'yxati: {nonushta}")
