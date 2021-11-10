# Tìm 2 số lớn nhất

numberList = [1,3,11,90,30,10,91,26,4,21]

i = len(numberList)
if i>2:
    numberList.sort(reverse=True)
    print("Hai số lớn nhất trong list đã cho là: ",numberList[0:2])
else:
    print("Hai số lớn nhất trong list đã cho là: ",numberList)