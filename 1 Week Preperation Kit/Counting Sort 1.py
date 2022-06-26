#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
##INCOMPLETE CODE
def countingSort(arr):
    # Write your code here
    n = len(arr)
    frequencyArr = [0 for i in range(100)]
    print(frequencyArr)
    # if((n>=100) and (n<=10**6)):
    #     isValid = 0
    #     for num in arr:
    #         if((num<0) or (num>100)):
    #             isValid+=1
    #             break
    #     if(isValid==0):
    #         for num in enumerate(arr):
    #             frequencyArr[num]+=1
    #         finalArr = []
    #         for i,frequency in enumerate(frequencyArr):
    #             finalArr.append(i)*frequency
    #         return finalArr
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
