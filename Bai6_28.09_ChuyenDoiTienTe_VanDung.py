# Ứng dụng chuyển đổi tiền tệ cho phép tính giá trị tiền tệ giữa các đồng tiền khác nhau dựa vào một tỉ giá cho trước
# Bước 1: Nhập số tiền USD cần đổi
# Bước 2: Nhập tỉ giá USD/VND 
# Bước 3: Tính toán ra số tiền VND theo tỉ giá và số tiền USD nhập vào bên trên
# Bước 4: In ra kết quả

Money = int(input("Nhập số tiền USD cần đổi:"))
TyGia = float(input("Nhập tỉ giá USD/VND:"))
print("Số tiền chuyển đổi sang VND:",Money*TyGia)