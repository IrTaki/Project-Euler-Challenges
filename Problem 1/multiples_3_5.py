"""
What we're trying to solve: https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

num_total = 0

for x in range(0, 1000):
    if (x % 3 == 0) or (x % 5 == 0):
        num_total += x

print("The total sum of all numbers that are multiples of 3 or 5 is:", num_total)
