"""
Problem: Count vowels in a string.
This program counts how many vowels (a, e, i, o, u) appear in a given string.
"""

# Count vowels in a string

text = "hello world"  # You can change this string

vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print(f"Number of vowels in '{text}': {count}")
