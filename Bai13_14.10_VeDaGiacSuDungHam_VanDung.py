# Xây dựng hàm vẽ hình đa giác đều với tham số là số cạnh của đa giác, và chiều dài của các cạnh. 
# Sau khi hàm được xây dựng xong, tiến hành gọi hàm với các giá trị tham số khác nhau.

import turtle

t= turtle.Turtle()
t.pensize(2)
t.pencolor("blue")

def polygons_draw(x,width):
    """Hàm vẽ hình đa giác đều
    x: số cạnh của đa giác đề
    width: chiều dài cạnh
    """
    # Giá trị mỗi góc của đa giác
    angle = 180 - (x-2)*180/x
    for i in range(x):
        t.forward(width)
        t.left(angle)

polygons_draw(5,100)