from itertools import combinations

s, n = map(str, input().split())
n = int(n)

mylist = list(s)
mylist = sorted(mylist)

for i in range(1, n + 1):
    clist = list(combinations(mylist, i))
    for j in clist:
        for k in range(i):
            print(j[k], end='')
        print()

