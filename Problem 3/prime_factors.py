"""
What we're trying to solve: https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math

prime_numbers = []
prime_factors = []
user_input = int(input("What number should I factorize? "))

# Divides the passed number by prime numbers until it cannot be divided anymore. 
def divide_by_prime(number):
    for x in prime_numbers:
        while number % x == 0 and number != 0:
            prime_factors.append(x)
            number //= x

# Runs a check to see if the factorized list multiplied together results in the users input or not.
def prime_factor_check(prime_factors):
    result = 1
    print(prime_factors)

    # Multiplies the contents of the list together.
    for x in prime_factors:
        result = x * result

    if result == user_input:
        print("The prime factors of {} are: ".format(str(user_input)), prime_factors)
    else:
        print("Error: The prime factors don't multiply to equal your input of {}.".format(str(user_input)))

# Gets all the prime numbers up to n+1 and adds them to a list.
for num in range(2, 10001):
    if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
        prime_numbers.append(num)

divide_by_prime(user_input)
prime_factor_check(prime_factors)