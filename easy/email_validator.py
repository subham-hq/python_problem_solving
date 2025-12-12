"""
Problem: Validate an email address using regular expressions (regex).

This script takes an email input from the user and checks whether it 
matches a valid email format using a predefined regex pattern. 
It supports domain extensions such as .com, .edu, and .net.

This beginner-friendly exercise helps reinforce:
- Basic regex usage with the 're' module
- Pattern matching and string validation
- Clean input handling and conditional logic
"""

import re

# Ask user for an email input
email = input("Enter your email: ")

# Regex pattern for validating email
pattern = r'[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)'

# Check if the email matches the pattern
if re.search(pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")
