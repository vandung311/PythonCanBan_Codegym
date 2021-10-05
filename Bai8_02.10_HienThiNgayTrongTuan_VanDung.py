#Hiển thị ngày trong tuần
# 1: Monday
# 2: Tuesday
# 3: Wednesday
# 4: Thursday
# 5: Friday
# 6: Saturday
# 7: Sunday
Number = int(input("Vui lòng nhập 1 số trong khoảng từ (1~7):"))
if(Number == 0 or Number > 7):
    print("error, out of range")
elif(Number==1):
    print("Monday")
elif(Number==2):
    print("Tuesday")
elif(Number==3):
    print("Wednesday")
elif(Number==4):
    print("Thursday")
elif(Number==5):
    print("Friday")
elif(Number==6):
    print("Saturday")
else:
    print("Sunday")