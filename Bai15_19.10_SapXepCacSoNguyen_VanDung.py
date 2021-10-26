# Viết chương trình cho người dùng nhập vào 3 số nguyên bất kỳ,
# sau đó sẽ in ra thứ tự tăng dần của 3 số nguyên được nhập vào.

def sort_nember(x,y,z):
    if(x>z and y>z):
        if(x>y):
            print(x,y,z)
        else:
            print(y,x,z)
    elif(x>y and z>y):
        if(x>z):
            print(x,z,y)
        else:
            print(z,x,y)
    else:
        if(y>z):
            print(y,z,x)
        else:
            print(z,y,x)

x = int(input("Nhập giá trị thứ 1: "))
y = int(input("Nhập giá trị thứ 2: "))
z = int(input("Nhập giá trị thứ 3: "))
sort_nember(x,y,z)