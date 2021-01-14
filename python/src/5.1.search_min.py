data = [6, 15, 8, 4, 8, 2, 11, 9, 7, 13]

min = 0
for i in range(1, len(data)):
    if data[min] > data[i]:
        min = i

print(min)
