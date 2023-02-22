class SHaxs:
    """ SHaxs uchun klsas"""

    def __init__(self, ism, familya, t_yil, davlat):
        """ SHaxsning xsusiyatlari"""
        self.name = ism
        self.surname = familya
        self.birth_year = t_yil
        self.age = 2023 - t_yil
        self.country = davlat

    def info(self):
        return f"Ism : {self.name} \nFamilya : {self.surname} \nYosh : {self.age} \nDavlat: {self.country}"


class Talaba(SHaxs):
    """ Talaba nomli klass"""
    def __init__(self, ism, familya, t_yil, davlat):
        self.ism = ism
        self.f 






shaxs1 = SHaxs("SHermuhammad", "Temirov", 2003, "O'zbekiston")
talaba1 = Talaba(shaxs1)
print(talaba1.ism)

# print(shaxs1.info())
    