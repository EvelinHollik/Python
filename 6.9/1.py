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
        if nap_nev == "0":
            print("Hétfő")
        elif nap_nev == "1":
            print("Kedd")
        elif nap_nev == "2":
            print("Szerda")
        elif nap_nev == "3":
            print("Csütörtök")
        elif nap_nev == "4":
            print("Péntek")
        elif nap_nev == "5":
            print("Szombat")
        elif nap_nev == "6":
            print("Vasárnap")
        elif nap_nev >= "7":
            print("None")
teszt.nap_nev(input("Adj meg egy számot: "))


#3

class teszt1:
    def nap_nev(nap_nev):
        if nap_nev == "Hétfő":
            print("0")
        elif nap_nev == "Kedd":
            print("1")
        elif nap_nev == "Szerda":
            print("2")
        elif nap_nev == "Csütörtök":
            print("3")
        elif nap_nev == "Péntek":
            print("4")
        elif nap_nev == "Szombat":
            print("5")
        elif nap_nev == "Vasárnap":
            print("6")
        else:
            print("None")
teszt1.nap_nev(input("Adj meg egy napot: "))
