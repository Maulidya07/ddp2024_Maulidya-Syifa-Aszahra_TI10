import bangun_datar_modul as bdm, aritmatika_modul as am, bangun_ruang_modul as brm
print('=== Program Perhitungan Matematika ===')
penghitungan = int(input("""Masukan Kategori matematika Kamu =  
1. Aritmatika
2. Luas Bangun Datar
3. Luas Bangun Ruang
(Pilih 1-3):  """))


#codingan jika pilih aritmatika
if penghitungan == 1:
        print("\nPilih operasi aritmatika yang ingin dilakukan:")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. Pangkat")
        pilihan = int(input("\nMasukkan nomor operasi aritmatika yang dipilih (1-5)"))

        if pilihan == 1:
            a = float(input("Masukkan angka pertama: "))
            b = float(input("Masukkan angka kedua: "))
            print(am.tambah(a,b))
        elif pilihan == 2:
            a = float(input("Masukkan angka pertama: "))
            b = float(input("Masukkan angka kedua: "))
            print(am.kurang(a,b))
        elif pilihan == 3:
            a = float(input("Masukkan angka pertama: "))
            b = float(input("Masukkan angka kedua: "))
            print(am.kali(a,b))
        elif pilihan == 4:
            a = float(input("Masukkan angka pertama: "))
            b = float(input("Masukkan angka kedua: "))
            print(am.bagi(a,b))
        elif pilihan == 5:
            a = float(input("Masukkan angka pertama: "))
            b = float(input("Masukkan angka kedua: "))
            print(am.pangkat(a,b))
        else:
            print("Pilihan Tidak Valid")
            
#codingan jika pilih bangun datar
elif penghitungan == 2:
    bd = int(input("""Pilih bangun datar yang ingin dihitung luasnya:
                1. Persegi
                2. Persegi Panjang
                3. Lingkaran
                4. Segitiga
                5. Jajargenjang
                Masukkan nomor operasi aritmatika yang dipilih (1-5)"""))

    match bd:
        case 1:
            print("Menghitung Luas Persegi")
            s = float(input("Masukkan sisi : "))
            bdm.luas_persegi(s)
        case 2:
            print("Menghitung Luas Persegi Panjang")
            p = float(input("Masukkan panjang : "))
            l = float(input("Masukkan lebar : "))
            bdm.luas_persegi_panjang(p,l)
        case 3:
            print("Menghitung Luas Lingkaran ")
            r = float(input("Masukkan jari-jari : "))
            bdm.luas_lingkaran(r)
        case 4:
            print("Menghitung Luas Segitiga")
            a = float(input("Masukkan alas : "))
            t = float(input("Masukkan tinggi : "))
            bdm.luas_segitiga(a,t)
        case 5:
            print("Menghitung Luas Jajargenjang")
            a = float(input("Masukkan alas : "))
            t = float(input("Masukkan tinggi : "))
            bdm.luas_jajargenjang(a,t)
        case _:
            print("Pilihan Tidak Valid")


#codingan jika pilih bangun ruang
elif penghitungan == 3:
    br = int(input("""
                Pilih bangun ruang yang ingin dihitung luasnya
                1. Kubus
                2. Balok
                3. Bola
                4. Kerucut
                5. Tabung
                Masukkan nomor operasi aritmatika yang dipilih (1-5)"""))

    match br:
        case 1:
            print("Menghitung Luas Kubus")
            s = float(input("Masukkan sisi : "))
            brm.luas_kubus(s)
        case 2:
            print("Menghitung Luas Balok")
            p = float(input("Masukkan panjang : "))
            l = float(input("Masukkan lebar : "))
            t = float(input("Masukkan tinggi : "))
            brm.luas_balok(p,l,t)
        case 3:
            print("Menghitung Luas Permukaan Bola")
            d = float(input("Masukkan diameter : "))
            brm.luas_permukaan_bola(d)
        case 4:
            print("Menghitung Luas Permukaan Kerucut")
            r = float(input("Masukkan jari-jari : "))
            s = float(input("Masukkan garis pelukis : "))
            brm.luas_permukaan_kerucut(r,s)
        case 5:
            print("Menghitung Luas Permukaan Tabung")
            r = float(input("Masukkan jari-jari : "))
            t = float(input("Masukkan tinggi : "))
            brm.luas_permukaan_tabung(r,t)
        case _:
            print("Pilihan Tidak Valid")

else:
    print("Pilihan Tidak Valid")