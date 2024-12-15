from Animal import Animal

class Ular(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, berbisa, bentuk_kepala):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.berbisa = berbisa
        self.bentuk_kepala = bentuk_kepala

    def info_ular(self):
        super().info_animal()
        print("Memiliki Bisa\t\t: ", self.berbisa,
              "\nBentuk Kepalanya\t: ", self.bentuk_kepala)

#objek
ular = Ular("Kobra", "Tikus", "Hutan Hujan Tropis, persawahan", "Bertelur", "Berbisa", "Segitiga")
print("===================================================")
print("## Info Ular##")
ular.info_ular()
ular = Ular("Piton", "Tikus, Rakun, Kelinci", "Hutan Hujan Tropis yang Lembab, Padang Rumput, Persawahan", "Bertelur", "Berbisa", "Segitiga")
print("===================================================")
print("## Info Ular##")
ular.info_ular()
ular = Ular("Anaconda", "Ikan, Katak, Burung, Mamalia dan Reptil", "Hutan Hujan Tropis, Rawa, dan Sungai", "Bertelur", "Tidak Berbisa", "Bulat agak lonjong")
print("===================================================")
print("## Info Ular##")
ular.info_ular()
ular = Ular("Kadut", "Ikan", "Sungai, Kolam berlumpur, Rawa-rawa", "Bertelur", "Tidak Berbisa", "Bulat agak lonjong")
print("===================================================")
print("## Info Ular##")
ular.info_ular()