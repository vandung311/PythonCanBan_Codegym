#Viết chương trình hỏi người dùng đã chi bao nhiêu tiền tại cửa hàng.
#Nếu họ chi ít hơn 75$, họ sẽ không được giảm giá.
#Nếu họ chi 75$ trở lên, họ sẽ được giảm giá 15$.
#Nếu người dùng chi từ 100$ trở lên, họ sẽ được giảm giá 25$.
#Nếu người dùng chi từ 150$ trở lên, họ sẽ được giảm giá 50$.
#Sau đó in ra tổng số tiền mà người dùng phải thanh toán.
Money = float(input("Bạn đã chi tiêu bao nhiêu tiền tại cửa hàng($):"))
if(Money<75):
    print("Bạn không được giảm giá")
    print("Số tiền cần thanh toán:",Money,"$")
elif(Money<100):
    print("Bạn được giảm giá 15$")
    print("Số tiền cần thanh toán:",Money-15,"$")
elif(Money<150):
    print("Bạn được giảm giá 25$")
    print("Số tiền cần thanh toán:",Money-25,"$")
else:
    print("Bạn được giảm giá 50$")
    print("Số tiền cần thanh toán:",Money-50,"$")