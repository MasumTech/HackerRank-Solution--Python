from collections import OrderedDict

n = int(input())

FOOD = OrderedDict()

for _ in range(0, n):
    *name, price = input().split()
    r = " ".join(name)

    if r not in FOOD:
        FOOD[r] = int(price)
    else:
        FOOD[r] += int(price)

for itemprices in FOOD:
    print(itemprices, FOOD[itemprices])