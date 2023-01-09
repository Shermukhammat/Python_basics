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
    def __init__(self, ism, familya, t_yil, davlat):
        super().__init__(ism, familya, t_yil, davlat)
        self.bosqich = 1






shaxs1 = SHaxs("SHermuhammad", "Temirov", 2003, "O'zbekiston")
talaba1 = Talaba(shaxs1)
print(talaba1.ism)

# print(shaxs1.info())
    