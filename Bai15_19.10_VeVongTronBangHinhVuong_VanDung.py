# Viết chương trình vẽ hình tròn bằng các hình vuông xoay quanh tâm điểm.

import turtle

square = turtle.Turtle()

def draw_square(step):
    square.speed(0.5)
    angle = 360/step
    for k in range(step):
        for i in range(3):
            square.forward(100)
            square.right(90)
        square.forward(100)
        square.right(90+angle)
    turtle.done()

draw_square(36)