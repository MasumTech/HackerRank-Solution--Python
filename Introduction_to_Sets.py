def average(array):
    sm = int(0)
    l = int(0)
    # your code goes here
    mylist = list(dict.fromkeys(array))
    l = int(len(mylist))
    for i in range(l):
        sm = sm + mylist[i]
    #print(sm, l)
    rst = (sm/int(l))
    return rst

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)