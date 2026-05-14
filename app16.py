# Kutubxona boshqaruv tizimi

class Kitob:
    def __init__(self, nomi, muallif, yil):
        self.nomi = nomi
        self.muallif = muallif
        self.yil = yil
        self.olingan = False

    def info(self):
        holat = "Band" if self.olingan else "Mavjud"
        return f"{self.nomi} | {self.muallif} | {self.yil} | {holat}"


class Kutubxona:
    def __init__(self, nomi):
        self.nomi = nomi
        self.kitoblar = []

    def kitob_qoshish(self, kitob):
        self.kitoblar.append(kitob)
        print(f"{kitob.nomi} kutubxonaga qo'shildi.")

    def kitoblar_royxati(self):
        print("\nKutubxonadagi kitoblar:")
        for i, kitob in enumerate(self.kitoblar, 1):
            print(f"{i}. {kitob.info()}")

    def kitob_olish(self, nom):
        for kitob in self.kitoblar:
            if kitob.nomi.lower() == nom.lower():
                if not kitob.olingan:
                    kitob.olingan = True
                    print(f"{kitob.nomi} olindi.")
                else:
                    print("Bu kitob band.")
                return
        print("Kitob topilmadi.")

    def kitob_qaytarish(self, nom):
        for kitob in self.kitoblar:
            if kitob.nomi.lower() == nom.lower():
                if kitob.olingan:
                    kitob.olingan = False
                    print(f"{kitob.nomi} qaytarildi.")
                else:
                    print("Bu kitob olinmagan.")
                return
        print("Kitob topilmadi.")


# Obyektlar yaratish
kitob1 = Kitob("Python Asoslari", "Ali Valiyev", 2024)
kitob2 = Kitob("Suniy Intellekt", "Bekzod Karimov", 2025)
kitob3 = Kitob("Dasturlash Sirlar", "Shoxrux", 2023)

# Kutubxona yaratish
kutubxona = Kutubxona("IT Kutubxona")

# Kitoblarni qo'shish
kutubxona.kitob_qoshish(kitob1)
kutubxona.kitob_qoshish(kitob2)
kutubxona.kitob_qoshish(kitob3)

# Ro'yxatni chiqarish
kutubxona.kitoblar_royxati()

# Kitob olish
kutubxona.kitob_olish("Python Asoslari")

# Yangilangan ro'yxat
kutubxona.kitoblar_royxati()

# Kitob qaytarish
kutubxona.kitob_qaytarish("Python Asoslari")

# Oxirgi holat
kutubxona.kitoblar_royxati()