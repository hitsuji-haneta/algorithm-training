def fizzbuzz():
    for i in range(100):
        target = i + 1

        result = target
        if target % (3 * 5) == 0:
            result = 'FizzBuzz'
        elif target % 3 == 0:
            result = 'Fizz'
        elif target % 5 == 0:
            result = 'Buzz'

        print(result, end=' ')
    print('')


fizzbuzz()
