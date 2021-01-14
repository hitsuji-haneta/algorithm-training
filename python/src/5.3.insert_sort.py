data = [6, 15, 8, 4, 8, 2, 11, 9, 7, 13]

for i in range(1, len(data)):
    tmp = data[i]
    j = i - 1
    while(j >= 0) and (data[j] > tmp):
        data[j+1] = data[j]
        j -= 1
    data[j+1] = tmp

print(data)
