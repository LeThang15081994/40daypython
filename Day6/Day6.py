
while(1):
    try: 
        time = int(input("Input your time: "))
        # sử dụng if else
        '''if time == 5:
            print("Wakeup")
        elif time == 6:
            print("Yoga")
        elif time == 7:
            print("Work")
        else:
            print("Do somthing else")
        # sử dụng dicnationary
        doing = {5:"Wakeup",6:"Yoga",7:"Work"}
        doing.get(time,"Do something else")'''
        # sử dụng Switch/case
        match time:
            case 5: 
                print("Wakeup")
            case 6:
                print("Yoga")
            case 7:
                print("Work")
            case _:
                print("Do somthing else")
        break
    except:
        print('Thông tin bạn nhập không hợp lệ')