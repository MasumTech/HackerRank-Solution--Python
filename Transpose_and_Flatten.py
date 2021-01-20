import numpy

m, n = map(int, input().split())
A = []

for i in range(m):
     a = [int(x) for x in input().split()]
     A.append(a)
# print(A)     

B = numpy.array(A)
print(numpy.transpose(B))
print(B.flatten())