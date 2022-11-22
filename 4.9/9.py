import turtle

Screen = turtle.Screen()
Teknos = turtle.Turtle()
Teknos.color("blue")
Screen.bgcolor("lightgreen")
Teknos.speed(5)
Teknos.pensize(1)

def csillag_rajzolas():
    for i in range(0,6):
        Teknos.right(144)
        Teknos.forward(100)
 
csillag_rajzolas()
Screen.mainloop()