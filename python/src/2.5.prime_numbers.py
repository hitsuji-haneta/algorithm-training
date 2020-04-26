import math
import sys


def is_prime(n):
    if not n > 1:
        return False

    if n == 2:
        return True

    max_number = math.ceil(math.sqrt(n))
    for i in range(2, max_number+1):
        if n % i == 0:
            return False
    return True


def get_prime_list(n):
    if not n > 1:
        return []

    confirmed = [2]
    check_max = math.ceil(math.sqrt(n))
    candidate = [i + 1 for i in range(2, n, 2)]
    while candidate[0] <= check_max:
        confirmed.append(candidate[0])
        candidate = [j for j in candidate if j % candidate[0] != 0]
    return confirmed + candidate


def main():
    input_string = input('number:')
    if not input_string.isdecimal():
        print('input must be integer')
        sys.exit()

    input_number = int(input_string)
    # for i in range(input_number):
    #     if is_prime(i):
    #         print(i, end=' ')
    # print()
    print(get_prime_list(input_number))


main()
