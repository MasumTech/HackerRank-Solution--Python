<<<<<<< HEAD
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split(" ")))

    m1 = max(arr)

    m2 = -9999999999

    for i in range(n):
        if arr[i] != m1 and arr[i] > m2:
            m2 = arr[i]
    print(m2)
=======

>>>>>>> cd7f4116d650d4a195373f18e2a2b3e9d873c344
