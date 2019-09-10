a = int(input())

if a%2==1:
    print("Weird")
elif a%2==0:
    if 2<=a and 5>=a:
        print("Not Weird")
    elif 6<=a and 20>=a:
        print("Weird")
    elif a>20:
        print("Not Weird")