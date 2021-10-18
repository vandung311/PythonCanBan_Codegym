# Xây dựng hàm vẽ hình tròn với tham số là bán kính. 
# Xây dựng tiếp hàm tính diện tích hình tròn với tham số là bán kính hình tròn. 
# Sau khi các hàm được xây dựng xong, tiến hành gọi các hàm với giá trị bán kính được nhập bởi người dùng.

import turtle
import math

t = turtle.Turtle()
t.pensize(3)
t.pencolor("blue")

def circle_draw(f):
    t.circle(f)

def circle_area(r):
    return math.pi*(r**2)

f = float(input("Nhập bán kính hình tròn:"))
circle_draw(f)
print("Diện tích hình tròn bán kính",f,"là:",circle_area(f))