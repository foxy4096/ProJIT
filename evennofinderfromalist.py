num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 25, 30]
index_list = []
even_num = []
for i in num:
    if i%2 == 0:
        index_list.append(num.index(i))
        even_num.append(i)

print(index_list)
print(even_num)
