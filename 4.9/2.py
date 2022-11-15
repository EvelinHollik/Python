import turtle

Screen = turtle.Screen()
Teknos = turtle.Turtle()

class teknos:
    def rajzol(fok,e):
        for i in range(0,4):
            Teknos.pendown()
            Teknos.forward(e)
            Teknos.left(fok)
            Teknos.penup()

a = turtle.Screen()
a.bgcolor("lightgreen")
Teknos.color("pink")
Teknos.pensize(3)

teknos.rajzol(90, 20)
Teknos.forward(20)
Teknos.left(90)
Teknos.back(10)
Teknos.right(90)
Teknos.forward(10)
Teknos.left(90)
teknos.rajzol(90, 40)
Teknos.forward(30)
Teknos.left(90)
Teknos.back(10)
Teknos.right(90)
Teknos.forward(20)
Teknos.left(90)
teknos.rajzol(90, 60)
Teknos.forward(40)
Teknos.left(90)
Teknos.back(10)
Teknos.right(90)
Teknos.forward(30)
Teknos.left(90)
teknos.rajzol(90, 80)
Teknos.forward(50)
Teknos.left(90)
Teknos.back(10)
Teknos.right(90)
Teknos.forward(40)
Teknos.left(90)
teknos.rajzol(90, 100)


Teknos.penup()
Teknos.forward(20)
Teknos.pendown()

Screen.mainloop()