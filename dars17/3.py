# 3. Quyidagi dasturda bir nechta mantiqiy xatolar bor. 
# Jumladan, xusisiy holatlarda tsikl abadiy qaytarilib
# qolmoqda. Xatolarni to'g'rilay olasizmi?

savol ="\nKiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
while True:
    qiymat = input(savol)
    if str(qiymat)=='exit':
        break
    elif int(qiymat)<0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"\n{qiymat} ning ildizi {ildiz} ga teng")