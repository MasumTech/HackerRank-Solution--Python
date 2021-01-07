from itertools import groupby

s = str(input())

for k, g in groupby(s):
    print('({}, {})'.format(len(list(g)), k), end=' ')

