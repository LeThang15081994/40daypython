#khởi tạo list từ 1 đến 10
lst_data = [data for data in range(1,11)]

#chuyển list sang string đôngg thời thêm "-"
lst_str = '-'.join(str(i) for i in lst_data)
print(lst_str,type(lst_str))

#Thực hiện ghi vào file data.txt
with open("data.txt","w") as f:
    f.write(lst_str)

#Câu 2
with open("data.txt","r") as f:
    map = list(f.read().split("-"))
    lst_fillter = [int(i) for i in map if int(i)%3 ==0]
print(lst_fillter)