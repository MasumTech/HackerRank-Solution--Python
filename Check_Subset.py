# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(input())):
    n = input()
    s = set(input().split())
    n1 = input()
    s1 = set(input().split())

    print(s.issubset(s1))