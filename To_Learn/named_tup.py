#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    count = 0
    for i in range(len(q)):
        j = i-1

        while j >= 0 and q[i] < q[j]:


            q[j], q[j+1] = q[j+1],q[j]

    print(q)



    # Write your code here

# if __name__ == '__main__':
#     t = int(input().strip())
#
#     for t_itr in range(t):
#         n = int(input().strip())
#
#         q = list(map(int, input().rstrip().split()))

minimumBribes([2, 1, 5, 3, 4])
