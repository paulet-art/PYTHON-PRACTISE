'''
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with

places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places,
'''



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    n = len(arr)
    count_positive = sum(1 for num in arr if num > 0)
    count_negative = sum(1 for num in arr if num < 0)
    count_zero = n - count_positive - count_negative
    
    ratio_positive = count_positive/n
    ratio_negative = count_negative/n
    ratio_zero = count_zero/n
    
    print("{:.6f}".format(ratio_positive))
    print("{:.6f}".format(ratio_negative))
    print("{:.6f}".format(ratio_zero))
    
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
