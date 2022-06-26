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
    if((n>0) and (n<=100)):
        isValid = 0
        for num in arr:
            if((num<-100) or (num>100)):
               isValid+=1
               break
        if(isValid==0):
            posCount = 0
            negCount = 0
            zeroCount = 0
            for num in arr:
                if(num>0):
                    posCount+=1
                elif(num<0):
                    negCount+=1
                else:
                    zeroCount+=1
            print("%0.6f" % (posCount/n))
            print("%0.6f" % (negCount/n))
            print("%0.6f" % (zeroCount/n))
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
