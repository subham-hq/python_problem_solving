"""
Problem: Calculate the factorial of a number.
This program computes the factorial using a simple loop.
"""

# Calculate factorial of a number

num = 5  # You can change this number
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"Factorial of {num} is: {factorial}")
