<<<<<<< HEAD
import turtle
screen = turtle.Turtle()
t=turtle.Turtle()

def rajzolj_oszlopot(t, magassag):
    szin(magassag)
    t.begin_fill()
    t.left(90)
    t.forward(magassag)
    if magassag < 0:
        t.penup()
        t.forward(-20)
        t.write(" "+ str(magassag))
        t.forward(20)
        t.pendown()
    else:
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
def szin(xs):
    if xs>=200:
        t.fillcolor("red")
    if xs>=100 and xs<200:
        t.fillcolor("yellow")
    if xs<100:
        t.fillcolor("green") 
    

ablak = turtle.Screen()
ablak.bgcolor("lightgreen")

t.color("blue")
t.pensize(3)

xs = [-48,117,-200,240,-160,260,220]

for m in xs:
    rajzolj_oszlopot(t, m)
szin(m)
=======
import turtle
screen = turtle.Turtle()
t=turtle.Turtle()

def rajzolj_oszlopot(t, magassag):
    szin(magassag)
    t.begin_fill()
    t.left(90)
    t.forward(magassag)
    if magassag < 0:
        t.penup()
        t.forward(-20)
        t.write(" "+ str(magassag))
        t.forward(20)
        t.pendown()
    else:
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
def szin(xs):
    if xs>=200:
        t.fillcolor("red")
    if xs>=100 and xs<200:
        t.fillcolor("yellow")
    if xs<100:
        t.fillcolor("green") 
    

ablak = turtle.Screen()
ablak.bgcolor("lightgreen")

t.color("blue")
t.pensize(3)

xs = [-48,117,-200,240,-160,260,220]

for m in xs:
    rajzolj_oszlopot(t, m)
szin(m)
>>>>>>> 2865ab6c45bd11627e8dbd0bbf1934f15233d767
screen.mainloop()