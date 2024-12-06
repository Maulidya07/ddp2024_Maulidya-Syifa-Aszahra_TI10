from Gempa import *

gempa1 = Gempa("Banten", 1.2)
gempa2 = Gempa("Palu", 6.1)
gempa3 = Gempa("Cianjur", 5.6)
gempa4 = Gempa("Jayapura", 3.3)
gempa5 = Gempa("Garut", 4.0)

#informasi gempa
print("## INFO GEMPA ##")
print()
gempa1.dampak()
print()
print("## INFO GEMPA ##")
gempa2.dampak()
print()
print("## INFO GEMPA ##")
gempa3.dampak()
print()
print("## INFO GEMPA ##")
gempa4.dampak()
print()
print("## INFO GEMPA ##")
gempa5.dampak()