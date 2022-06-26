#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def insertionSort(arr):
    n = len(arr)
    for i,num in enumerate(arr):
        key = arr[i]
        j = i-1
        while((j>=0) and (arr[j]>key)):
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key

def findMedian(arr):
    # Write your code here
    n = len(arr)
    if(((n>=1)and(n<=1000001))and(n%2==1)):
        isValid = 0
        if((arr[0]<-10000) or (arr[-1]>10000)):
            isValid+=1
        if(isValid==0):
            insertionSort(arr)
            medianIndex = n//2
            return arr[medianIndex]
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
