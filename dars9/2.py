#2

"""
2.Yuqoridagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan 
xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)
"""

ismlar = ['anvar', 'akmal', 'shaxzod', 'xamdam', 'rasul', 'begzod']
son = 0

for ism in ismlar[:]:
	son += 1
	print('--------------------')
	print(f"Salom {ism.title()}. Xush kelibsiz!")
	print('--------------------')
print(f"Kod {son} marta takrorlandi")