class Mobil: #osztály
    Csörög = "csörög"
    Kikapcsol = "kikapcsol"
    Bekapcsol = "bekapcsol"

def Csörög (telefon): #1.metódus
    print (telefon, Csörög)
def Kikapcsol (telefon): #2.metódus
    print (telefon, Kikapcsol)
def Bekapcsol (telefon): #3.metódus
    print (telefon, Bekapcsol)

Mobil.Bekapcsol("A telefon")
Mobil.Csörög("A telefon")
Mobil.Kikapcsol("A telefon")