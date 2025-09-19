#Given a string,S, of length N that is indexed from 0 to N-1 , print its even-indexed and odd-indexed characters as  space-separated strings on a single line (see the Sample below for more detail).
#Note:0 is considered to be an even index.

# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input("Enter number of test cases: "))

for _ in range(T):
    s = input("Enter characters: ")
    even = s[::2]
    odd = s[1::2]
    print(f"{even} {odd}")