#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    n = len(a)
    if((n>=1) and (n<=100)):
        isValid = 0
        for num in a:
            if((num<0) or (num>100)):
                isValid+=1
                break
        if(isValid==0):
            for num in a:
                if a.count(num)==1:
                    return num    
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
