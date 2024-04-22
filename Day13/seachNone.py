lst_data = [1,1.1,None,1.4,None,1.5,None,2.0]
lst_idx =[]

for i in range(len(lst_data)):
    if lst_data[i] == None:
        lst_idx.append(i)
print(f"Vị trí None đầu tiên : {lst_idx[0]} - Danh sách vị trí có giá trị None {lst_idx}")        
