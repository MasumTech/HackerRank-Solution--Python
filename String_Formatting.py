def print_formatted(number):
    # your code goes here
    w = len(str(bin(number)).replace('0b', ''))
    for i in range(1, number + 1):
        print(str(i).rjust(w, ' '), end=' ')
        print((oct(i).replace("0o", "")).rjust(w, ' '), end=' ')
        print((hex(i).replace("0x", "").upper()).rjust(w, ' '), end=' ')
        print((bin(i).replace("0b", "")).rjust(w, ' '), end=' ')
        print()


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)