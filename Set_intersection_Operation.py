# Enter your code here. Read input from STDIN. Print output to STDOUT

a = input()
s1 = set(input().split())

b = input()
s2 = set(input().split())

sfinal = s1.intersection(s2)
print(len(sfinal))
