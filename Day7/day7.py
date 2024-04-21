list_data = [0,2,4,6,8,10,12]
 
for i in list_data:
    if i % 3==0:
        list_data.remove(i)
print(list_data)

for i in [1,2,3]:
    list_data.append(i)
print(list_data)

j = 3
for i in [6,7,8]:
    list_data.insert(j,i)
    j+=1
print(list_data)

for i in range(len(list_data)):
    if list_data[i] %2 == 0 or list_data[i] % 5 ==0:
        list_data[i] = 0

print(list_data)
        