"""
What we're trying to solve: https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

prime_numbers = []
x = 2
user_input = int(input("What number should I go up to? "))

# We call this function to find out if the passed number is
# a prime number and return True or False based on
# the result.
def is_prime(n):
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True

# Checks what the prime numbers are between 2 and the user input.
# If is_prime returns true, it appends it to the prime_numbers list.
while x <= user_input:
    if is_prime(x):
        prime_numbers.append(x)
    x += 1

print(prime_numbers[:])
