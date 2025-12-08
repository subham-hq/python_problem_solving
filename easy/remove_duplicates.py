"""
Problem: Remove duplicates from a list.
This program removes repeated values from a list using Python's set() method.
"""

# Remove duplicates from a list

numbers = [1, 2, 2, 3, 4, 4, 5]

unique_numbers = list(set(numbers))

print(f"Original list: {numbers}")
print(f"List after removing duplicates: {unique_numbers}")
