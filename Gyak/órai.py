#print("Helló, Világ")

#print(6+4*9)

#print("Szeretjük a Python teknőcöket!")
#for i in range(1000):
#print("Szeretjük a Python teknőcöket!")
#xs=(12, 10, 32, 3, 66, 17, 42, 99, 20)
#print("12, 10, 32, 3, 66, 17, 42, 99, 20")

print("Teknőcök")
import turtle
ablak =turtle.Screen()
ablak.bgcolor("lightgreen")
Eszti = turtle.Turtle()
Eszti.shape("turtle")
szinek = ["white", "pink", "red", "purple"]
Eszti.speed(100)

Eszti.penup()
meret=2
index=0
for i in range (1000):
    Eszti.stamp()
    meret=meret+3
    Eszti.forward(meret)
    Eszti.right(24)
    Eszti.color(szinek[index])
    if index==3:
        index=0
    else:
        index=index+1


ablak.mainloop()