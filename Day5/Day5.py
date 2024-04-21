list_data = [1,2,3,4,5,6,7,8,9,10]

print(list_data[0:5])
print([i  for i in list_data if i%2==0 ])
result = 0 
for i in list_data:
    result += i
print(result)