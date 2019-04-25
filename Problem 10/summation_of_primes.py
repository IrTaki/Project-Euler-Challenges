"""
What we're trying to solve: https://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import math

prime_numbers = 2

# Gets all the prime numbers up to n+1 and adds up the result.
for num in range(3, 2000001, 2):
    if all(num % i != 0 for i in range(3, int(math.sqrt(num)) + 1)):
        prime_numbers += num
        print(num)

print("The total sum of all prime numbers below 2,000,000 is: ", prime_numbers)