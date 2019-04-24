"""
What we're trying to solve: https://projecteuler.net/problem=6
"""

sum_of_squares = 0
square_of_sum = 0

for x in range(1, 101):
    sum_of_squares += x * x

for y in range(1, 101):
    square_of_sum += y

square_of_sum = square_of_sum * square_of_sum
print(sum_of_squares)
print(square_of_sum)

print("The answer is: ", square_of_sum - sum_of_squares)
