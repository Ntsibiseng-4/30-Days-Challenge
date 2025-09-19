#Given the meal price (base cost of a meal), tip percent (the percentage of the meal price 
#being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost. 
# Round the result to the nearest integer.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
    tip = meal_cost/100 * tip_percent
    tax = tax_percent/100 * meal_cost
    total_cost = meal_cost + tip + tax
    print("The total cost of the meal is:", round(total_cost))
    
if __name__ == '__main__':
    meal_cost = float(input("Enter meal cost:").strip())
    tip_percent = int(input("Enter tip: ").strip())
    tax_percent = int(input("Enter tax: ").strip())
    solve(12.00, 20, 8)
    