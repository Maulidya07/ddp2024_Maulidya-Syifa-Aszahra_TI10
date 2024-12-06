import math

def luas_kubus(s):
    luas = 6*s**2
    print("Luas kubus dengan sisi", s," = ", luas)

def luas_balok(p,l,t):
    luas = 2*(p*l+p*t+t*l)
    print("Luas persegi panjang dengan panjang ", p, " , lebar ", l, " dan tinggi ", t," = ", luas)

def luas_permukaan_bola(d):
    luas = math.pi*d**2
    print("Luas permukaan bola dengan diameter ", d, " = ", luas)

def luas_permukaan_kerucut(r,s):
    luas = math.pi*r*(s+r)
    print("Luas permukaan kerucut dengan jari-jari ", r, " dan garis pelukis ", s, " = ", luas)

def luas_permukaan_tabung(r,t):
    luas = 2*math.pi*r*(r+t)
    print("Luas permukaan tabung dengan jari-jari ", r, " dan tinggi ", t, " = ", luas)