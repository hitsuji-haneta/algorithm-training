import sys


def calc_change(change):
    amountList = [10000, 5000, 2000, 1000, 500, 100, 50, 10, 5, 1]
    dict = {}
    for amount in amountList:
        number_of_currency, change = divmod(change, amount)
        dict[amount] = number_of_currency
    return dict


insert_price = input('insert: ')
if not insert_price.isdecimal():
    print('insert_price must be integer')
    sys.exit()

product_price = input('product: ')
if not product_price.isdecimal():
    print('product_price must be integer')
    sys.exit()

change = int(insert_price) - int(product_price)
if change < 0:
    print('shortage of fees')
    sys.exit()

print(f'change: {change}')
print(calc_change(change))
