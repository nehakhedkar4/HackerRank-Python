''' You are the manager of a supermarket.
You have a list of N items together with their prices that consumers bought on a particular day.
Your task is to print each item_name and net_price in order of its first occurrence. '''

from collections import OrderedDict

n = int(input())
items = OrderedDict()

for i in range(n):
    item, price = input().rsplit(' ', 1)
    price = int(price)
    items[item] = items.get(item, 0) + price

for item, price in items.items():
    print(item, price)
