x = int(input("Elso oldal:"))
y = int(input("Masodik oldal:"))
c = int(input("Harmadik oldal(a legnagyobb):"))

def derekszogu_e():
    if (x**2)+(y**2)==(c**2):
        print("A hámoszög derékszögű")
    else:
        print("A háromszög nem derékszögű")

derekszogu_e()