#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    # print(s,n)
    # print(s*n)
    # count=0
    if s=="a":
        count=n
        return count
    elif (len(s)==1 and s!="a"):
        return 0
    
    string=(s*n)
    cache={}
    for i in range(n):
        if string[i]=="a" not in cache:
            cache[i]="a"
           
    return(len(cache))
     

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
