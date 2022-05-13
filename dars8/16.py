#16.ikkala ro'yhatni ham (taomlar va
#nonushta) konsolga chiqaring.

taomlar = ['osh', 'manti', 'sho\'rva', 'somsa', 'kabob']

nonushta = taomlar[:]

#print(f"nonushta ro'yxati: {nonushta}")

nonushta.remove('osh')
del nonushta[0]
nonushta.append('CHoy')
nonushta.insert(0, 'Sut')


print(f"taomlar ro'yxati : {taomlar}")
print(f"nonushta ro'yxati : {nonushta}")