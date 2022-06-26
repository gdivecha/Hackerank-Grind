#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
import math

def diagonalDifference(arr):
    # Write your code here
    n = len(arr)
    isValid = 0
    for i in range(0,n):
        for j in range(0,n):
            if((arr[i][j]<-100)or(arr[i][j]>100)):
                isValid+=1
                break
    if(isValid==0):
        diag1Sum = 0
        diag2Sum = 0
        for i in range(0,n):
            diag1Sum+=(arr[i][i])
        count = n-1
        for i in range(0,n):
            diag2Sum+=(arr[i][count])
            count-=1
        return abs(diag1Sum - diag2Sum)
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
