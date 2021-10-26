# Viết chương trình cho phép người dùng nhập chuỗi và và hiển thị số ký tự trong chuỗi vừa nhập vào.

def count_chars(txt):
    result = 0
    for i in txt:
        result += 1
    return result

input_str = input("Nhập chuỗi: ")
print("Độ dài của chuỗi: ", count_chars(input_str))