list_shopping = ["carot","tao","sua"]

for i in range(len(list_shopping)):
    print(f"{i+1}.{list_shopping[i]}")

for index, item in enumerate(list_shopping,start=1):
    print(f"{index}.{item}")

food_list = [
            ["bo","pizza","sua"],
            ["xucxich","tao","kem"],
            ["carot","banhdau","cupcake"]

]

food_seach = ["carot","tao","sua"]

for index_h,item_1 in enumerate(food_list):
    for index_w,item_2 in enumerate(item_1):
        if item_2 in food_seach:
            print(f"{item_2} được tìm thấy ở hàng {index_h} và cột {index_w}")