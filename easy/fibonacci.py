"""
Problem: Print Fibonacci series.
This program prints the first 'n' numbers in the Fibonacci sequence.
"""

# Print Fibonacci series

n = 10  # Number of terms to print

a, b = 0, 1

print("Fibonacci Series:")

for _ in range(n):
    print(a)
    a, b = b, a + b
