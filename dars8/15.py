#15.Yangi ro'yhatda faqat nonushtaga 
# yeyiladiag taomlarni qoldiring, va 
# qo'shimcha yangi 2ta taom kriting.

taomlar = ['osh', 'manti', 'sho\'rva', 'somsa', 'kabob']

nonushta = taomlar[:]

print(f"nonushta ro'yxati: {nonushta}")

nonushta.remove('osh')
del nonushta[0]
nonushta.append('CHoy')
nonushta.insert(0, 'Sut')

print(f"nonushta ro'yxatiga ishlo'v berlgach: {nonushta}")