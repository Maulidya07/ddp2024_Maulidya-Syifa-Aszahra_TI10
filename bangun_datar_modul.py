import math

def luas_persegi(s):
    luas = s*s
    print("Luas persegi dengan sisi", s," = ", luas)

def luas_persegi_panjang(p,l):
    luas = p*l
    print("Luas persegi panjang dengan panjang ", p, " dan lebar ", l," = ", luas)

def luas_lingkaran(r):
    luas = math.pi*r**2
    print("Luas lingkaran dengan jari-jari ", r, " = ", luas)

def luas_segitiga(a,t):
    luas = 0.5*a*t
    print("Luas segitiga dengan alas ", a, " dan tinggi ", t, " = ", luas)

def luas_jajargenjang(a,t):
    luas = a*t
    print("Luas jajargenjang dengan alas ", a, " dan tinggi ", t, " = ", luas)