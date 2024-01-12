#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    is_pm = "P" in s
    h = s[0:2]
    
    if is_pm and int(h) != 12:
        h = str(int(h)+12)
    elif not is_pm and int(h) == 12:
        h = "00"
    
    return f"{h}{s[2:8]}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
