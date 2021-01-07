x, y = map(int, input().split())

# print(x, y)

A = []

for _ in range(y):
    A.append(map(float, input().split()))
    # print(A)

for i in zip(*A):
    # print(i)
    print(sum(i) / len(i))