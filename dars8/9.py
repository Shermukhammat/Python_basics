#9.ro'yhatdagi sonlar yig'indisini hsoblang va
# konsolga chiqaring.

juft_sonlar = list(range(120, 1201,2))

ygndi = 0
z = 0
for n in juft_sonlar:
    z=z+1
    ygndi+=n
    print(z, ':    ', n)
print('ro\'yxat elementlari yg\'indsi ', ygndi, 'ga teng!')
