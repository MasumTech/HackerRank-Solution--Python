from collections import namedtuple

n = int(input())
fields = input().split()
# print(fields)
total = 0
for i in range(n):
    students = namedtuple('student', fields)
    field1, field2, field3, field4 = input().split()
    student = students(field1, field2, field3, field4)
    total += int(student.MARKS)
    # print(total)
avg = total / n
print('{:.2f}'.format(avg))
