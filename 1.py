#1
#class teszt:
#    def irany(irany):
#        irany= input("Adj meg egy égtájat (é,k,d,ny)")
#        if irany == "é" and "É":
#            print("Kelet")
#        elif irany == "k" and "K":
#            print("Dél")
#        elif irany == "d" and "D":
#            print("NYugat")
#        elif irany == "ny" and "NY":
#            print("Észak")
#        else:
#            print("none")
#        return irany
#teszt.irany()

#2
#class teszt1:
#    def nap_nev(nap_nev):
#        if nap_nev == "0":
#            print("Hétfő")
#        elif nap_nev == "1":
#            print("Kedd")
#        elif nap_nev == "2":
#            print("Szerda")
#        elif nap_nev == "3":
#            print("Csütörtök")
#        elif nap_nev == "4":
#            print("Péntek")
#        elif nap_nev == "5":
#            print("Szombat")
#        elif nap_nev == "6":
#            print("Vasárnap")
#        else:
#            print("None")
#teszt1.nap_nev(input("Adj meg egy számot: "))

#3
#class teszt2:
#    def nap_nev(nap_nev):
#        if nap_nev == "Hétfő":
#            print("0")
#        elif nap_nev == "Kedd":
#            print("1")
#        elif nap_nev == "Szerda":
#            print("2")
#        elif nap_nev == "Csütörtök":
#            print("3")
#        elif nap_nev == "Péntek":
#            print("4")
#        elif nap_nev == "Szombat":
#            print("5")
#        elif nap_nev == "Vasárnap":
#            print("6")
#        else:
#            print("None")
#teszt2.nap_nev(input("Adj meg egy napot: "))

#4
#def nap():
#    nap = ["hétfő", "kedd", "szerda", "csütörtök", "péntek", "szombat", "vasárnap"]
#    mikor = int(input("Hány nap múlva? "))
#    napIn = input("melyik nap indulsz? ").lower()
#    napIndex = None
#
#    for i in range(0, len(nap)):
#        if napIn == nap[i].lower():
#            napIndex = i
#    szam = (napIndex+mikor)%7
#
#    print ("Ma", napIn, "van, és", mikor, "nap múlva nyaralni megyek vagyis", nap[szam])
#
#nap()

#5
#def napok():
#    nap = ["hétfő", "kedd", "szerda", "csütörtök", "péntek", "szombat", "vasárnap"]
#    mikor = int(input("Hány nap múlva? "))
#    napIn = input("melyik nap indulsz? ").lower()
#    napIndex = None
#
#    for i in range(0, len(nap)):
#        if napIn == nap[i].lower():
#            napIndex = i
#    szam = (napIndex+mikor)%7
#
#    print ("Ma", napIn, "van, és", mikor, "napon mentél vagyis", nap[szam])
#
#napok()

#6
#class teszt3:
#    def honap_napja(honap_napja):
#        if honap_napja == "január":
#            print("31")
#        elif honap_napja == "február":
#            print("28")
#        elif honap_napja == "március":
#            print("31")
#        elif honap_napja == "április":
#            print("30")
#        elif honap_napja == "május":
#            print("31")
#        elif honap_napja == "június":
#            print("30")
#        elif honap_napja == "július":
#            print("31")
#        elif honap_napja == "augusztus":
#            print("31")
#        elif honap_napja == "szeptember":
#            print("30")
#        elif honap_napja == "október":
#            print("31")
#        elif honap_napja == "november":
#            print("30")
#        elif honap_napja == "december":
#            print("31")
#        else:
#            print("None")
#teszt3.honap_napja(input("Adj meg egy hónapot: "))

#7
#def masodpercre_valtas():
#    ora =int(input("Add meg az órát: "))
#    perc =int(input("Add meg az percet: "))
#    masodperc =int(input("Add meg az másodpercet: "))
#    orak= ora * 3600
#    perck= perc * 60
#    masodpercek = orak + perck + masodperc
#    print(ora, "óra +", perc, "perc +", masodperc, "másodperc =", masodpercek, "másodperc")
#masodpercre_valtas()

#8
#def masodpercre_valtas2():
#    ora =float(input("Add meg az órát: "))
#    perc =float(input("Add meg az percet: "))
#    masodperc =float(input("Add meg az másodpercet: "))
#    orak= ora * 3600
#    perck= perc * 60
#    masodpercek = orak + perck + masodperc
#    print(int(ora), "óra +", int(perc), "perc +", int(masodperc), "másodperc =", int(masodpercek), "másodperc")
#masodpercre_valtas2()

#9
#def orara_valtas():
#    masodperc = int(input("másodperc: "))
#    ora = masodperc/3600
#    orak = masodperc%3600
#    perc = orak/60
#    perk = orak%60
#    masodpercek = perk
#    print(int(ora)," óra",int(perc),"perc",masodpercek,"másodperc")
#orara_valtas()

#10


#11
# def osszehasonlitas():
#     a=int(input("Adj meg egy számot: "))
#     b=int(input("Adj meg egy számot: "))

#     if a > b:
#         print ("1")
#     elif a == b:
#         print("0")
#     elif a < b:
#         print("-1")
# osszehasonlitas()

#12
#class teszt4:
#    def atfogo():
#        bef1 = int(input("1. befogó: "))
#        bef2 = int(input("2. befogó: "))
#        atfogo = ((bef1*bef1)+(bef2*bef2)) ** 0.5
#        print(atfogo)
#print(teszt4.atfogo())

#13
#class teszt5:
#    def meredekseg(x1,y1,x2,y2):
#        return (y1-y2)/(x1-x2)
#        print(meredekseg(5,3,4,2))
#        print(meredekseg(1,2,3,2))
#        print(meredekseg(1,2,3,3))
#        print(meredekseg(2,4,1,2))
#        print(meredekseg(1,6,3,12))
#teszt5.meredekseg()

#14
#class teszt6:
#    def paros_e(n):
#        if n%2 == 0: return True
#        else: return False
#print(teszt6.paros_e())

#15
#class teszt7:
#    def paratlan_e(n):
#        if n%2 !=0:
#            return True
#        else:
#            return False
#print(teszt7.paratlan_e())

#16
#class teszt8:
#    def tenyezo_e(t, n):
#        if n%t==0: return True
#        else: return False
#print(teszt8.tenyezo_e())

#17
#class teszt9:
#    def tobbszorose_e(t, n):
#        if t%n==0:
#            return True
#        else:
#            return False
#print(teszt9.tobbszorose_e())

#18
#class teszt10:
#    def celsiusra_valtas(f):
#        return int(((f-32)/9)*5)
#print(teszt10.celsiusra_valtas)

#19
#class teszt11:
#    def Fahrenheit_valtas(c):
#        return int(((c/5)*9)+32)
#print(teszt11.Fahrenheit_valtas)