from collections import Counter

n = int(input())
mylist = list(map(int, input().strip().split()))[:n]
mylist = Counter(mylist)
earn = 0
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    if mylist[x] > 0:
        earn += y
        mylist[x] -= 1

print(earn)
