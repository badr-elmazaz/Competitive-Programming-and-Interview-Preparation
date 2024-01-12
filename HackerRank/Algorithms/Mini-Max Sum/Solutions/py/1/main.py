#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # time  -> O(nlogn)
    # space -> O(n)
    
    arr.sort()
    
    minimum = sum(arr[0:-1])
    maximum = sum(arr[1::])

    
    print(minimum, maximum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
