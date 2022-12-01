import turtle

Screen = turtle.Screen()
Teknos = turtle.Turtle()

a = turtle.Screen()
a.bgcolor("lightgreen")
Teknos.color("pink")

for i in range(5):
    Teknos.pensize(3)
    Teknos.left(90)
    Teknos.forward(20)
    Teknos.left(90)
    Teknos.forward(20)
    Teknos.left(90)
    Teknos.forward(20)
    Teknos.left(90)
    Teknos.forward(20)
    Teknos.left(90)

Teknos.penup
Teknos.forward(20)
Teknos.pendown

Screen.mainloop()