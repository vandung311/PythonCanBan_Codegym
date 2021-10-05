#Nhập vào 1 số nguyên bất kì. Kiểm tra số nguyên nhập vào có chia hết cho 2 hay không?
#Nếu chia hết cho 2: số chẵn
#Nếu không chia hết cho 2 có dư : số lẻ
Number = int(input("Nhập vào số nguyên bất kỳ:"))
X = "Số bạn nhận vào là số chẵn" if Number%2 == 0 else "Số bạn nhập vào là số lẻ"
print(X)