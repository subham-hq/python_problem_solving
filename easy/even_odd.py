"""
Problem: Check if a number is even or odd.
This program takes an integer input and determines whether it is even or odd
using the modulus (%) operator.
"""

# Check if a number is even or odd

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
