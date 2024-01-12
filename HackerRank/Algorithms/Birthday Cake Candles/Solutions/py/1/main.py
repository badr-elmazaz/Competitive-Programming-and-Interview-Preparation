#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # time ->  O(n)
    # space -> O(1)
    
    maximum = candles[0]
    counter_maximum = 1
    
    for i in range(1, len(candles)):
        if candles[i] > maximum:
            maximum = candles[i]
            counter_maximum = 1
        elif candles[i] == maximum:
            counter_maximum += 1
            
    return counter_maximum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
