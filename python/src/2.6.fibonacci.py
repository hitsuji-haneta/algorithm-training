import sys


def fibonacci(n):
    if n <= 0:
        return []
    if n <= 1:
        return [1]
    if n <= 2:
        return [1, 1]

    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib


def fib_memo(n):
    if n <= 0:
        return {}
    if n <= 1:
        return {1: 1}
    if n <= 2:
        return {1: 1, 2: 1}

    memo = {1: 1, 2: 1}
    for i in range(2, n):
        memo = add_fib_memo(i+1, memo)

    return memo


def add_fib_memo(n, memo):
    memo[n] = memo[n-1] + memo[n-2]
    return memo


def main():
    input_string = input('number:')
    if not input_string.isdecimal():
        print('input must be a integer')
        sys.exit()

    input_number = int(input_string)
    print(fibonacci(input_number))
    print(fib_memo(input_number))


main()
