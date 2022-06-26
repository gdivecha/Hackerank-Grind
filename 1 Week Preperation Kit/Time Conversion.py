#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    string = ""
    timeMode = s[8:10].lower()
    hour = (10*int(s[0]))+(int(s[1]))
    if(timeMode=="am"):
        if(int(hour==12)):
            string = "00" + s[2:8] 
        else:
            string = s[0:8]
    elif(timeMode=="pm"):
        if(int(hour==12)):
            string = s[0:8] 
        else:
            string = str(hour+12) + s[2:8]
    return string

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
