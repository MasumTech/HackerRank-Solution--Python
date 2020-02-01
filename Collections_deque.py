# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
n = int(input())
arr = deque()
for i in range(n):
    inpt = input().split()
    if len(inpt)==2:
        actn = inpt[0]
        e = inpt[1]
        #print(actn, e)
    elif len(inpt)==1:
        actn = inpt[0]
        #print(actn)

    if actn=='append':
        arr.append(e)
    elif actn=='appendleft':
        arr.appendleft(e)
    elif actn=='pop':
        arr.pop()
    elif actn=='popleft':
        arr.popleft()
    elif actn=='clear':
        arr.clear()
    elif actn=='extend':
        arr.extend(e)
    elif actn=='remove':
        arr.remove(e)
    elif actn=='rotate':
        arr.rotate(e)
    elif actn=='reverse':
        arr.reverse()

for j in range(len(arr)):
    print(arr[j], end=' ')
