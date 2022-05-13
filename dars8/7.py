#7.sort() metodi yordamida ro'yhatni avval
# alifbo bo'yicha, keyin esa alifboga 
# teskari tartibda konsolga chiqaring.


davlatlar = ['AQSH', 'Rossiya', 'Germanya', 'Xitoy', 'Turkiya', 'Italiya', 'albanya']



print(f"\ndavlatlar ro'yxati{davlatlar}")
davlatlar.sort()
print(f"\ndavlatlar ro'yxati .sort() metodi bilan: {davlatlar}")
davlatlar.sort(reverse=True)
print(f"\ndavlatlar ro'yxati .sort(reverse=True) metodi bilan:{davlatlar}")
