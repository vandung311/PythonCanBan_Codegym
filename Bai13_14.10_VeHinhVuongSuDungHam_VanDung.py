# Xây dựng hàm vẽ hình vuông với tham số là độ dài các cạnh. Sau khi 
# hàm được xây dựng xong, tiến hành gọi hàm với các giá trị tham số khác nhau.
import turtle

t= turtle.Turtle()
t.pensize(2)
t.pencolor("blue")

def square_draw(x):
    for i in range(4):
        t.forward(x)
        t.left(90)

square_draw(100)