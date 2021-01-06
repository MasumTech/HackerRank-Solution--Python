n = int(input())
flist = {int(x) for x in input().split()}
# print(flist)

m = int(input())
slist = {int(x) for x in input().split()}
# print(slist)

rlist = flist.difference(slist)
rslist = slist.difference(flist)
# print(rlist)
# print(rslist)

result = sorted(rlist.union(rslist))
for i in result:
   print(i)