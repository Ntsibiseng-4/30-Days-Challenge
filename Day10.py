# Given a base-10 integer n, convert it to binary (base-2).
# Then find and print the maximum number of consecutive 1's in n's binary representation.

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    print("Enter a base-10 integer to find the maximum number of consecutive 1's in its binary representation:")
    n = int(input().strip())

    # Convert to binary and remove the '0b' prefix
    binary = bin(n)[2:]

    # Split by '0' to isolate sequences of '1's
    ones_groups = binary.split('0')

    # Find the longest sequence
    max_consecutive_ones = max(len(group) for group in ones_groups)
    print(max_consecutive_ones)
