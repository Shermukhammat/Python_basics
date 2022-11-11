

""" LAMBDA funksiyasi """
# import math

# lambda argument : ifoda

# uzunlik = lambda pi, r : 2*pi*r
# print(uzunlik(math.pi, 10))

# kvadrat = lambda x, y : x**y
# print(kvadrat(3, 2))

# def daraja(n):
# 	return lambda x : x**n
# print(daraja(3))
# kvadrat = daraja(2)
# print(kvadrat(5))
# kub = daraja(3)
# print(kub(5))

""" MAP funksiyasi """

from math import sqrt

sonlar = list(range(1,11))
ildizlar = list(map(sqrt, sonlar))

