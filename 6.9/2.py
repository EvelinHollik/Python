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