import sys


def convert(decimal, base):
    result = ''
    while decimal > 0:
        result = str(decimal % base) + result
        decimal = decimal // base
    return result


decimal_number = input('decimal: ')
if not decimal_number.isdecimal():
    print('decimal_number must be integer')
    sys.exit()

base_number = input('base: ')
if not base_number.isdecimal():
    print('base_number must be integer')
    sys.exit()

print(convert(int(decimal_number), int(base_number)))
