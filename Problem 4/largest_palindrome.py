"""
What we're trying to solve: https://projecteuler.net/problem=4

A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

calculating = True
palindrome_list = [0]

# Checks if the number passed to it is a palindrome and if it is
# compares it against the last highest palindrome in the list before
# appending it or skipping it.
def check_if_palindrome(number):
    reversed_number = ""
    for c in str(number):
        reversed_number = c + reversed_number
    
    if str(number) == str(reversed_number) and number > palindrome_list[0]:
        palindrome_list.append(number)
        del palindrome_list[0]

# Main loop
while calculating:
    for x in range(100, 1000):
        for y in range(100, 1000):
            total = x * y
            check_if_palindrome(total)
    calculating = False

print(palindrome_list)