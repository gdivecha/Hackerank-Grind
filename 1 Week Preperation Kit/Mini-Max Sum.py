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

def insertionSort(arr):
    n = len(arr)
    for i,num in enumerate(arr):
        key = arr[i]
        j = i-1
        while((j>=0) and (arr[j]>key)):
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key

def miniMaxSum(arr):
    # Write your code here
    isValid = 0
    for num in arr:
        if((num<1) or (num>((10**9)))):
            isValid+=1
    if(isValid==0): 
        insertionSort(arr)
        minimum = arr[0] + arr[1] + arr[2] + arr[3];
        maximum = arr[-1] + arr[-2] + arr[-3] + arr[-4];
        print(f"{minimum} {maximum}")
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
