m , n = map(int, input().split())
# print(m, n)

for i in range(1,m,2):
    print((i*'.|.').center(n,'-'))
print('WELCOME'.center(n, '-'))
for i in range(m-2, -1, -2):
    print((i*'.|.').center(n,'-'))
