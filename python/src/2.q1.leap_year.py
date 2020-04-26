import sys


def check_leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def main():
    input_string = input('year: ')
    if not input_string.isdecimal():
        print('year must be an integer')

    for i in range(int(input_string)+1):
        if check_leap(i):
            print(i, end=' ')
    print()


main()
