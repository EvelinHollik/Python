<<<<<<< HEAD
import turtle
screen = turtle.Turtle()
t=turtle.Turtle()

def rajzolj_oszlopot(t, magassag):
    t.begin_fill()
    t.left(90)
    t.forward(magassag)
    t.write("  "+ str(magassag))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(magassag)
    t.left(90)
    t.end_fill()
    t.penup()
    t.forward(10)
    t.pendown()

ablak = turtle.Screen()
ablak.bgcolor("lightgreen")

Eszti = turtle.Turtle()
Eszti.color("blue", "red")
Eszti.pensize(3)

xs = [48,117,200,240,160,260,220]

for m in xs:
    rajzolj_oszlopot(Eszti, m)


=======
import turtle
screen = turtle.Turtle()
t=turtle.Turtle()

def rajzolj_oszlopot(t, magassag):
    t.begin_fill()
    t.left(90)
    t.forward(magassag)
    t.write("  "+ str(magassag))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(magassag)
    t.left(90)
    t.end_fill()
    t.penup()
    t.forward(10)
    t.pendown()

ablak = turtle.Screen()
ablak.bgcolor("lightgreen")

Eszti = turtle.Turtle()
Eszti.color("blue", "red")
Eszti.pensize(3)

xs = [48,117,200,240,160,260,220]

for m in xs:
    rajzolj_oszlopot(Eszti, m)


>>>>>>> 2865ab6c45bd11627e8dbd0bbf1934f15233d767
screen.mainloop()