# Enter your code here. Read input from STDIN. Print output to STDOUT

n = input()
s = set(input().split())
n1 = input()
s1 = set(input().split())

tt = s.symmetric_difference(s1)

print(len(tt))