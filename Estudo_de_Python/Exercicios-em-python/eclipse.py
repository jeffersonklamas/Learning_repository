# ----------------------------------------
# Criando eclipses de cores.

import turtle
col = ("yellow","red","green","blue","white","orange","pink","gray","lilac","purple","brown")

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t.speed(30)

for i in range (150):
    t.color(col[i%6])
    t.forward(i*6)
    t.left(150)
    t.width(2)