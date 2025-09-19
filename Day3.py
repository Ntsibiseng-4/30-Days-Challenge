#Given an integer,n, perform the following conditional actions:
#If n is odd, print Weird
#If n is even and in the inclusive range of  to 2, 5 print Not Weird
#If n is even and in the inclusive range of  to 6, 20 print Weird
#If n is even and greater than 20, print Not Weird
#Complete the stub code provided in your editor to print whether or not n is weird.

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input("Enter n value: ").strip())

if n%2 !=0:
    print("Weird")
elif n%2 ==0 and n in range(2, 6):
    print("Not Weird")
elif n%2 ==0 and n in range(6, 21):
    print("Weird")
elif n%2 ==0 and n>20:
    print("Not Weird")
else:
    print("Even or odd number entered!")