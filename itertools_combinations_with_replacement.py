# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations_with_replacement

string = input().split(' ')

str1 = string[0]
s1 = []
for i in range(len(str1)):
    s1.append(str1[i])
s1.sort()
# print(s1)
e = int(string[1])

if e == 1:
    for i in range(len(s1)):
        print(s1[i])
else:
    li = list(combinations_with_replacement(s1, e))

    # print(str(li))

    li1 = []

    for i in range(len(li)):
        lttr = ''
        for j in range(e):
            lttr = lttr + li[i][j]
        li1.append(lttr)
    li1.sort()
    # print(li1)

    for i in range(len(li1)):
        print(li1[i])

