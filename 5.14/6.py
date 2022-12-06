xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

def jegy():
    for x in xs:
        if x < 60:
            print("A jegyed elégtelen vagyis 1-es")
        
        if x>=60 and x<=70:
            print("A jegyed elégséges vagyis 2-es")
        
        if x>=70 and x<=80:
            print("A jegyed közepes vagyis 3-mas")

        if x>=80 and x<=90:
            print("A jegyed jó vagyis 4-es")

        if x>=90 :
            print("A jegyed jeles vagyis 5-ös")

jegy()