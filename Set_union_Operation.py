# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
set_1 = set(map(int, input().split(" ")))
#print(set_1)

n1 = int(input())
set_2 = set(map(int, input().split(" ")))
#print(set_2)


print(len(set_1.union(set_2)))
#print(set_1.union(set_2))
