import sys


def convert(binary):
    result = 0
    for i in range(len(binary)):
        digit = len(binary) - 1 - i
        result += int(binary[i]) * (2 ** digit)
    return result


def isBinary(string):
    return all([elm == '0' or elm == '1' for elm in string])


binary_number = input('binary: ')
if not isBinary(str(binary_number)):
    print('binary_number must be binary')
    sys.exit()

print(convert(str(binary_number)))
