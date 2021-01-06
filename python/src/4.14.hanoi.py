def hanoi(n, src, dis, via):
    if n > 1:
        hanoi(n-1, src, via, dis)
        print(src + '->' + dis)
        hanoi(n-1, via, dis, src)
    else:
        print(src + '->' + dis)


print('the number of hight => ', end='')
n = int(input())
hanoi(n, 'a', 'b', 'c')
