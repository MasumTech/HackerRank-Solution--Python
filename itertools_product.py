# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

a = map(int, input().split())
b = map(int, input().split())

li = list(product(a,b))
li.sort()

for i in range(len(li)):
    print(li[i], end=' ')
