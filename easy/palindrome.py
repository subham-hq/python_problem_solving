"""
Problem: Check if a string is a palindrome.
This program takes a string and determines whether it reads the same 
forward and backward using Python's slicing technique.
"""

# Check if a string is a palindrome

text = "madam"  # You can change this string

reversed_text = text[::-1]

if text == reversed_text:
    print(f'"{text}" is a palindrome.')
else:
    print(f'"{text}" is not a palindrome.')
