if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(N):
        inputs = input().split()
        if len(inputs) == 1:
            cmd = inputs[0]
        elif len(inputs) == 2:
            cmd = inputs[0]
            e = int(inputs[1])
        elif len(inputs) == 3:
            cmd = inputs[0]
            e = int(inputs[1])
            i = int(inputs[2])

        if cmd == 'insert':
            arr.insert(e, i)
        elif cmd == 'remove':
            arr.remove(e)
        elif cmd == 'append':
            arr.append(e)
        elif cmd == 'pop':
            arr.pop()
        elif cmd == 'sort':
            arr.sort()
        elif cmd == 'reverse':
            arr.reverse()
        elif cmd == 'print':
            print(arr)
