import turtle

Screen = turtle.Screen()
Teknos = turtle.Turtle()
Teknos.color("black")
Screen.bgcolor("lightgreen")
Teknos.speed(5)
Teknos.pensize(5)

Teknos.right(90)
def kor_terulet(r):
    for i in range(0,36):
        Teknos.forward(r)
        Teknos.left(10)

kor_terulet(15)
Screen.mainloop()
