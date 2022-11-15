import turtle

Screen = turtle.Screen()
Teknos = turtle.Turtle()

class teknos:
    def rajzol(fok,e):
        for i in range(0,4):
            Teknos.forward(e)
            Teknos.left(fok)

a = turtle.Screen()
a.bgcolor("lightgreen")
Teknos.color("pink")
Teknos.pensize(3)

ablak = turtle.Screen()
Eszti = turtle.Turtle()
Eszti.right(90)
Eszti.left(3600)
Eszti.right(-90)
Eszti.speed(10)
Eszti.left(3600)
Eszti.speed(0)
Eszti.left(3645)
Eszti.forward(-100)

Teknos.penup()
Teknos.forward(20)
Teknos.pendown()

Screen.mainloop()