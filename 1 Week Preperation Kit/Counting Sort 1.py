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

def countingSort(arr):
    # Write your code here
    n = len(arr)
    if((n>=100)and(n<=10**6)):
        isValid = 0
        if(isValid==0):
            frequencyArr = [0 for x in range(n)]
            isValid = 0
            for num in arr:
                if((num<0)or(n>100)):
                    isValid+=1
                    break
                frequencyArr[num]+=1
                # print(frequencyArr)
            if(isValid==0):
                # print(len(frequencyArr))
                return frequencyArr
            #Following lines of code actually return the sorted array
            # finalArr = []
            # for i,frequency in enumerate(frequencyArr):
            #     for j in range(frequency):
            #         finalArr.append(i)
            # return finalArr
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
