# Luyện tập cách xây dựng hàm, sử dụng hàm, các lệnh vẽ, tùy chỉnh bút vẽ trong thư viện turtle.

import turtle

t = turtle.Turtle()

def home_draw(x,y):
    t.pencolor("blue")
    for j in range(2):
        for k in range(1,3):
            t.fillcolor("pink")
            t.begin_fill()
            t.penup()
            if(j==0):
                t.goto(x*(k-1),0)
            else:
                t.goto(x*(k-1),y)
            t.pendown()
            for i in range(2):
                t.forward(x)
                t.left(90)
                t.forward(y)
                t.left(90)
            t.end_fill()
            a = (x/3)+x*(k-1)
            b = (y/3)+j*y
            t.penup()
            t.goto(a,b)
            t.pendown()
            t.fillcolor("white")
            t.begin_fill()
            for i in range(2):
                t.forward(x/3)
                t.left(90)
                t.forward(y/3)
                t.left(90)
            t.end_fill()
            t.penup()
            t.goto(x,0)
            t.pendown()
        t.penup()
        t.goto(x*j,y)
        t.pendown()

    t.penup()
    t.goto(x*2,0)
    t.pendown()
    t.fillcolor("pink")
    t.begin_fill()
    for i in range(2):
        t.forward(x*1.5)
        t.left(90)
        t.forward(y)
        t.left(90)
    t.end_fill()

    for r in range(2):
        t.fillcolor("brown")
        t.begin_fill()
        t.penup()
        t.goto(x*2+(x*1.5/4)*(r+1),0)
        t.pendown()
        for s in range(2):
            t.forward((x*1.5)/4)
            t.left(90)
            t.forward(y/2)
            t.left(90)
        t.end_fill()

home_draw(100,150)