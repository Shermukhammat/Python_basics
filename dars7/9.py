"""
9.Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.


"""

friends = ['Dilshod', 'Faxriddin', 'Faxriddin', 'Xudayberdi', 'Abdulaziz', 'Suxrob']
print('friends:',friends)

orta = int(len(friends) / 2)
 


friends.insert(orta, 'laziz')
friends.append('Mahmud')
friends.insert(0, 'Samandar')

print(friends)