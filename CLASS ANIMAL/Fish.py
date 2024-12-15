from Animal import Animal

class Fish(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, bernapas, habitat):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.bernapas = bernapas
        self.habitat = habitat

    def info_fish(self):
        super().info_animal()
        print("Bernapas menggunakan\t: ", self.bernapas,
              "\nHabitat Di\t\t: ", self.habitat)

#objek
fish = Fish("Hiu", "Daging", "laut", "Bertelur dan Melahirkan", "Insang", "Air Asin")
print("===================================================")
print("## Info Fish##")
fish.info_fish()
fish = Fish("Paus Biru", "Ikan", "laut", "Melahirkan", "Paru-Paru", "Air Tawar")
print("===================================================")
print("## Info Fish##")
fish.info_fish()
fish = Fish("Ikan Badut", "Zooplankton", "laut", "Bertelur", "Insang", "Terumbu Karang")
print("===================================================")
print("## Info Fish##")
fish.info_fish()
fish = Fish("Lumba-lumba", "Ikan", "laut", "Melahirkan", "Paru-Paru", "Air Asin dan Tawar")
print("===================================================")
print("## Info Fish##")
fish.info_fish()