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
