#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    print("Enter 6 rows of 6 space-separated integers each (for the 6x6 array):")
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
        
    max_sum = -63 # The min value per cell is -9, and 7 cells in an hourglass > -9*7=-63

    for i in range(4): # rows 0 to 3
        for j in range(4): # columns 0 to 3
            top = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            mid = arr[i+1][j+1]
            bot = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            hourglass = top + mid + bot
            max_sum = max(max_sum, hourglass)
    print("Maximum hourglass sum:", max_sum)