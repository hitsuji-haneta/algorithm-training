data = [6, 15, 8, 4, 8, 2, 11, 9, 7, 13]

for i in range(len(data)):
    for j in range(len(data) - i - 1):
        if data[j] > data[j+1]:
            data[j], data[j+1] = data[j+1], data[j]

print(data)
