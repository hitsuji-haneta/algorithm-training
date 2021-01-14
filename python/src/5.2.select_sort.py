data = [6, 15, 8, 4, 8, 2, 11, 9, 7, 13]


def search_min(data, base_index):
    start = base_index + 1
    min_index = base_index
    for i in range(start, len(data)):
        if data[min_index] > data[i]:
            min_index = i
    return min_index


for i in range(len(data)):
    min = search_min(data, i)
    data[i], data[min] = data[min], data[i]

print(data)
