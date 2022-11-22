napok = ["Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap"]
nap = int(input("Hány napra mész el? "))
szam=0
szam= nap%7
print(nap[szam-1])