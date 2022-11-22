import turtle

Screen = turtle.Screen()
Teknos = turtle.Turtle()
Teknos.color("black")
Screen.bgcolor("lightgreen")
Teknos.speed(5)
Teknos.pensize(5)

def szabalyos_haromszog_rajzolas(t, sz):
    for i in range(0,3):
        Teknos.forward(150)
        Teknos.left(sz)

szabalyos_haromszog_rajzolas(Teknos, 120)
Screen.mainloop()