def Calculate(x, y):
    try:
        result = (int(x) / int(y))
        print(int(result))

    except ZeroDivisionError as e:
        print('Error Code: integer division or modulo by zero')

    except ValueError as e:
        print('Error Code:', e)


n = input()

for i in range(int(n)):
    a, b = map(str, input().split())
    Calculate(a, b)
