cube = lambda x: x ** 3  # complete the lambda function

def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        a = 0
        b = 1
        l = [0, 1]
        for i in range(3, n + 1):
            c = a + b
            a = b
            b = c
            l.append(c)
        return l

        # return a list of fibonacci numbers


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
