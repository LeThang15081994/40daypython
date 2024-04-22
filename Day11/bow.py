corpus = ["Tôi thích môn toán", "Tôi thích AI","Tôi thích âm nhạc"]
sample = "Tôi thích AI thích toán"
#c1
map = []
list_dic= []

for i in corpus:
    map.append(i.split())

for i in map:
    for j in i:
        if j in list_dic:
            continue
        else:
            list_dic.append(j)

sample_vec = [0]*len(list_dic)
sample_word = sample.split()
for i in range(len(sample_word)):
    if sample_word[i] in list_dic:
        sample_vec[list_dic.index(sample_word[i])] +=1
    
print(f"Cách 1:\n {list_dic} \n {sample_vec}")
#print(sample_word.index("toán"))

#c2
map = []
list_dic= []

map = ' '.join(corpus)
list_dic = list(set(map.split()))
sample_vec = [0]*len(list_dic)
sample_word = sample.split()
#print(list_dic)
for w in sample_word:
    #print(list_dic.index(w))
    sample_vec[list_dic.index(w)] +=1
print(f"Cách 2:\n {list_dic} \n {sample_vec}")
