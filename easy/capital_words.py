"""
Problem: Extract all words that start with a capital letter.

This script scans a sentence and identifies every word that 
begins with an uppercase letter (A–Z). It uses regular 
expressions to match capitalized words while ignoring punctuation.

This exercise helps reinforce:
- Regex basics using the 're' module
- Word boundary detection
- Text processing and pattern matching
"""

import re

# Sample sentence
sentence = "Hello, I am Subham and I Live in India."

# Regex to match words starting with a capital letter
pattern = r'\b[A-Z][a-zA-Z]*\b'

# Extract matching words
capital_words = re.findall(pattern, sentence)

print(capital_words)
