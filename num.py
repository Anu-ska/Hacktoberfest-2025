# Write a Python program to find all the numbers in a given list that are perfect squares.
# A perfect square is a number that is the square of an integer (e.g., 4 = 2², 9 = 3², 16 = 4²).

# Example:
# Input: [4, 5, 9, 12, 16, 20, 25]
# Output: [4, 9, 16, 25]

import math

def find_perfect_squares(numbers):
    perfect_squares = []
    for num in numbers:
        root = math.sqrt(num)
        if root == int(root):  # check if square root is a whole number
            perfect_squares.append(num)
    return perfect_squares

# Example input
numbers = [4, 5, 9, 12, 16, 20, 25]
result = find_perfect_squares(numbers)

print("Perfect squares in the list:", result)
