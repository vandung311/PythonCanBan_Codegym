# Trò chơi 21 là trò chơi số đếm được bắt đầu từ 0, hai người chơi lần lượt có thể thêm 1, 2 hoặc 3, vào tổng số. 
# Tổng số không được vượt quá 21 và người chơi đếm tới 21 sẽ thua. 
# Ở bài tập này, chúng ta sẽ giả định cho máy làm người chơi thứ 2.

import random
while(True):
    i = int(random.randint(0,1))
    sum = 0
    if(i == 0):
        while(True):
            number_computer = int(random.randint(1,3))
            print("lựa chọn của máy tính là:",number_computer)
            sum += number_computer
            if(sum>21):
                print("Computer thua cuộc","Và","Người chơi chiến thắng")
                break
            else:
                human_player = int(input("Nhập giá trị của người chơi:"))
                while(human_player==0 or human_player>3):
                    print("Giá trị người chơi nhập không chính xác, chỉ nhập giá trị 1~3")
                    human_player = int(input("Nhập giá trị của người chơi:"))
                sum += human_player
                if(sum>21):
                    print("Người chơi thua cuộc","Và","Computer chiến thắng")
                    break
    else:
        while(True):
            human_player = int(input("Nhập giá trị của người chơi:"))
            while(human_player==0 or human_player>3):
                print("Giá trị người chơi nhập không chính xác, chỉ nhập giá trị 1~3")
                human_player = int(input("Nhập giá trị của người chơi:"))
            sum += human_player
            if(sum>21):
                print("Người chơi thua cuộc","Và","Computer chiến thắng")
                break
            else:
                number_computer = int(random.randint(1,3))
                print("lựa chọn của máy tính là:",number_computer)
                sum += number_computer
                if(sum>21):
                    print("Computer thua cuộc","Và","Người chơi chiến thắng")
                    break
    play_again = input("Bạn có muốn chơi lại hay không (Y/N):")
    if(play_again == "Y" or play_again == "y"):
        continue
    else:
        break