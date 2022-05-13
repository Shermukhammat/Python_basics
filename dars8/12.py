#12.Ro'yhatning boshidan, o'rtasidan va oxiridan
# 20ta qiymatni konsolga chiqaring

juft_s = list(range(120, 1201,2))

uzunlik = len(juft_s)
orta = int(uzunlik / 2)
start = orta - 10
stop = orta + 10

print(f"Ro'yxat boshi :{juft_s[0:20]}")
print(f"Ro'yxat o'rtasi : {juft_s[start:stop]}")
print(f"Ro'yxat oxri : {juft_s[-20: ]}")
