"""
10.Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va 
.append() metodlari yordamida mehmonga kelgan do'stlaringizning 
ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga
qo'shing
"""

friends = ['Dilshod', 'Faxriddin', 'Faxriddin', 'Xudayberdi', 'Abdulaziz', 'Suxrob']

mehmonlar = []
print(f"friends: {friends}\n"
	f"mehmonlar: {mehmonlar}\n")


ism = friends [1]

mehmonlar.insert(0, friends.pop(4))
mehmonlar.insert(1, friends.pop(-1))
mehmonlar.insert(2, friends.pop(0))
mehmonlar.insert(3, friends.pop(0))
mehmonlar.append(ism)


print(f"friends: {friends}\n"
	f"mehmonlar: {mehmonlar}\n")