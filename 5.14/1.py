napok = [ "Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap" ]

try:
    napIndex = int(input("Hány napra mész el? "))
    print(napok[napIndex - 1])
except:
    print("Nem helyes formátum!")