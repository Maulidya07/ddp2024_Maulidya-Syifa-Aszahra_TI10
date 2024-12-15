from Animal import Animal

class Bird(Animal):
    #Konstruktor properti
    def __init__(self, name, makanan, hidup, berkembang_biak, warna, paruh):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.warna = warna
        self.paruh = paruh

    #method
    def info_bird(self):
        super().info_animal()
        print("Warna\t\t\t: ", self.warna,
              "\nJenis Paruh\t\t: ", self.paruh)

#objek
bird = Bird("Elang", "Daging", "Ditebing", "Bertelur", "Coklat", "Bengkok dan Lancip")
print("================================================================")

print("## Info Bird")
bird.info_bird()
bird = Bird("Penguin", "Ikan", "Di Antartika", "Bertelur", "Hitam Putih/Abu-abu Putih", "Panjang dan Lancip")
print("================================================================")
print("## Info Bird")
bird.info_bird()
bird = Bird("Burung Unta", "Rumput, daun, buah, biji-bijian dan akar", "Digurun", "Bertelur", "Coklat keabu-abuan dan Putih", "Tak Bergigi dan Lancip")
print("================================================================")
print("## Info Bird")
bird.info_bird()
bird = Bird("Beo", "Buah-buahan, biji-bijian, dan serangga", "Didataran tinggi", "Bertelur", "Campuran warna merah, kuning, biru, dan oranye", "Melengkung")
print("================================================================")
print("## Info Bird")
bird.info_bird()