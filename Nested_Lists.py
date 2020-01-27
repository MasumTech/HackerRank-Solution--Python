if __name__ == '__main__':
    li = []
    n = int(input())
    for _ in range(n):
        name = input()
        score = float(input())
        li.append([name, score])

    li.sort(key=lambda x: x[0])

    li.sort(key=lambda x: x[1])

    second = float(0.00)
    for i in range(n):
        if li[0][1] > float(0.0):
            if li[0][1] < li[i][1]:
                second = li[i][1]

                break

        else:
            if li[0][1] < li[i][1]:
                second = li[i][1]

                break

    for i in range(n):
        if second == li[i][1]:
            print(li[i][0])


