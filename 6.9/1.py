#1
class teszt:
    def irany(irany):
        if irany == "é" and "É":
            print("Kelet")
        elif irany == "k" and "K":
            print("Dél")
        elif irany == "d" and "D":
            print("NYugat")
        elif irany == "ny" and "NY":
            print("Észak")
        else:
            print("none")
        return irany

teszt.irany("é")

#2
class teszt:
    def nap_nev(nap_nev):
        int(input("Adj meg egy számot: "))
        if nap_nev == "0":
            print("Hétfő")
        if nap_nev == "1":
            print("Kedd")
        if nap_nev == "2":
            print("Szerda")
        if nap_nev == "3":
            print("Csütörtök")
        if nap_nev == "4":
            print("Péntek")
        if nap_nev == "5":
            print("Szombat")
        if nap_nev == "6":
            print("Vasárnap")
        if nap_nev >= "7":
            print("None")
 
teszt.nap_nev()

#3
class teszt:
    def nap_nev(nap_nev):
        int(input("Adj meg egy napot: "))
        if nap_nev == "Hétfő":
            print("0")
        if nap_nev == "Kedd":
            print("1")
        if nap_nev == "Szerda":
            print("2")
        if nap_nev == "Csütörtök":
            print("3")
        if nap_nev == "Péntek":
            print("4")
        if nap_nev == "Szombat":
            print("5")
        if nap_nev == "Vasárnap":
            print("6")

teszt.nap_nev()