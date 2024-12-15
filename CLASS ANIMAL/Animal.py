class Animal:
    #konstruktor properti
    def __init__(self, name, makanan, hidup, berkembang_biak):
        self.name = name
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak
    #method informasi
    def info_animal(self):
        print("Nama Hewan\t\t: ", self.name, 
              "\nMakanan\t\t\t: ", self.makanan,
              "\nHidup\t\t\t: ", self.hidup,
              "\nBerkembang Biak\t\t: ", self.berkembang_biak)
        
# objek
kucing = Animal("Kucing", "Daging", "Hidup", "Melahirkan")

kucing.info_animal()