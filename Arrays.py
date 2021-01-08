import numpy

def arrays(arr):
    b = numpy.array(arr,float)
    return b[::-1]

arr = raw_input().strip().split(' ')
result = arrays(arr)
print(result)