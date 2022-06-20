# 1. Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini 
# hisoblaydigan funksiya yozing.

def tavallud() :
	""" Isim va yoshni so'rab tug'lgan yilni aniqlovchi funksiya!"""

	ism999 = input('Ismingiz nima ?\n>>>')
	yosh999 = int(input(f"{ism999.title()}nyoshinigiz nechida? \n>>>"))

	tugulgan_yil999 = 2022 - yosh999
	print(f"{ism999.title()} siz {tugulgan_yil999}-yilda tug'ulgan ekansiz!	")

tavallud()