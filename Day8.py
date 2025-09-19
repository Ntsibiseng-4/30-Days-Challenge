#Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. 
# You will then be given an unknown number of names to query your phone book for. For each name queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; 
# if an entry for name is not found, print Not found instead.

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

print("Enter the number of entries, followed by each name and phone number (space separated). Then enter names to query, one per line:")

#Read number of enteries
n = int(input())

#Build the phone book dictionary
phone_book = {}
for _ in range(n):
    entry = input().split()
    name = entry[0]
    number = entry[1]
    phone_book[name] = number
    

for line in sys.stdin:
    query = line.strip()
    if query in phone_book:
        print(f"{query}={phone_book[query]}")
    else:
        print("Not found")
