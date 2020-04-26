import sys


def get_gengou(year):
    if not between(num=year, start=1869, end=2020):
        return 'year must be between 1869 and 2020.'
    if between(num=year, start=1868, end=1911):
        return f'明治{year - 1868 + 1}年'
    if between(num=year, start=1912, end=1925):
        return f'大正{year - 1812 + 1}年'
    if between(num=year, start=1926, end=1988):
        return f'昭和{year - 1926 + 1}年'
    if between(num=year, start=1989, end=2018):
        return f'平成{year - 1989 + 1}年'
    if between(num=year, start=2019, end=2020):
        return f'令和{year - 2019 + 1}年'
    return 'error'


def between(num, start, end):
    if (start <= num) and (num <= end):
        return True
    return False


def main():
    input_string = input('year: ')
    if not input_string.isdecimal():
        print('year must be an intger.')
        sys.exit()

    input_number = int(input_string)
    print(get_gengou(input_number))


main()
