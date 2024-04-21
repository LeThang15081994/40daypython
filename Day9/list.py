#Tạo list
list_data = list(range(1,11))
print(list_data)
#tính trung vị của list

if len(list_data) % 2 == 0:
    #nếu độ dài list là số chẵn
    print("Median: ", (list_data[int(len(list_data)/2)-1] + list_data[int(len(list_data)/2)])/2)
else:
    #nếu độ dài list là số lẻ
    print("Median: ", list_data[(len(list_data)+1)/2])

list_odd_fillter = sorted([i for i in list_data if i % 2 !=0],reverse=True)

print(list_odd_fillter)