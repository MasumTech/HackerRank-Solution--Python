import re

def checker(regex):
    try: re.compile(regex)
    except re.error:
        return False
    return True

for i in range(int(input())):
    print(checker(input()))