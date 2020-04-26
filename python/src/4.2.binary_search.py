import sys


def binary_search(num, data):
    left = 0
    right = len(data) - 1
    while left < right:
        mid = int((left + right)/2)
        if num < data[mid]:
            right = mid - 1
        elif data[mid] < num:
            left = mid + 1
        else:
            return mid
    return -1


def main():
    data = [10, 20, 30, 40, 50, 60, 70]
    input_string = input('number:')
    if not input_string.isdecimal():
        print('input must be a integer')
        sys.exit()

    input_number = int(input_string)
    index = binary_search(input_number, data)
    print(f'index: {index}')


main()
