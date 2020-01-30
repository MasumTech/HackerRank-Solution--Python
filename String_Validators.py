if __name__ == '__main__':
    s = input()
    alnum = int(0)
    alpha = int(0)
    dgt = int(0)
    lwr = int(0)
    upr = int(0)

    for i in s:
        if i.isalnum() == True:
            alnum = int(1)
        else:
            alnum = int(0)
        if i.isalpha() == True:
            alpha = int(1)

        if i.isdigit() == True:
            dgt = int(1)

        if i.islower() == True:
            lwr = int(1)

        if i.isupper() == True:
            upr = int(1)

    if alnum == 1:
        print("True")
    else:
        print("False")
    if alpha == 1:
        print("True")
    else:
        print("False")
    if dgt == 1:
        print("True")
    else:
        print("False")
    if lwr == 1:
        print("True")
    else:
        print("False")
    if upr == 1:
        print("True")
    else:
        print("False")

