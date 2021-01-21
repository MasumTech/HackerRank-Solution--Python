import calendar

m, d, y = map(int, input().split())
# print(m, d, y)

weekday = calendar.weekday(y,m,d)

print(calendar.day_name[weekday].upper())
                                
                               