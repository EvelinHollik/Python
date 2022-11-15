import turtle

screen = turtle.Screen()
Eszti = turtle.Turtle()

class negyzet_rajzol:
    def negyzet_rajzol(t, h):
        for i in range(0,t):
            t.forward(h)
            t.left(90)

a = turtle.Screen()
a.bgcolor("lightgreen")
Eszti.color("blue")
Eszti.pensize(5)

meret=20
for i in range(15):
    negyzet_rajzol(Eszti, meret)
    Eszti.forward(10)
    Eszti.right(18)

a.mainloop()