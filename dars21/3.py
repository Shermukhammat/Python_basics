"""
3.Darsimiz davomida yozgan bahola funksiyasini .pop() metodidan 
foydalanmasdan va asl ro'yxatga o'zgartirish kiritmasdan faqat 
lug'at qaytaradigan qilib yozing.
"""

def bahola(ismlar):
	baholar = {}
	for ism in ismlar:
		baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
		baholar[ism] = int(baho)
	return baholar

talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar)
print(baholar)
