#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    ss = ''
    s1 = s
    for i in range(len(s1)):
        if s1[i].isdigit()==True:
            ss = ss + s1[i]
        elif s1[i-1]==' ' and s1[i].isalpha()==True:
            ss = ss + s1[i].upper()
        elif i==0:
            ss = ss + s1[i].upper()
        else:
            ss = ss + s1[i]
    return ss

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
