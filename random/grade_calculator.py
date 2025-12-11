"""
Simple grade calculator based on a numeric score between 0.0 and 1.0.
The program assigns a letter grade using standard threshold logic.
"""

score = input("Enter Score: ")

try:
    score = float(score)
except ValueError:
    print("Please provide numeric input.")
    exit()

if 0.9 <= score <= 1.0:
    print("A")
elif 0.8 <= score < 0.9:
    print("B")
elif 0.7 <= score < 0.8:
    print("C")
elif 0.6 <= score < 0.7:
    print("D")
elif 0.0 <= score < 0.6:
    print("F")
else:
    print("Score is out of range, please provide a value between 0.0 and 1.0.")
