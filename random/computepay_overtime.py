"""
Function to compute gross pay with overtime.
Normal rate applies up to 40 hours, and time-and-a-half applies
to any hours worked beyond 40.
"""

def computepay(hours, rate):
    if hours > 40:
        pay = (40 * rate) + ((hours - 40) * (rate * 1.5))
    else:
        pay = hours * rate
    return pay

# User input
hours_inp = input("Enter hours: ")
rate_inp = input("Enter rate per hour: ")

try:
    hours = float(hours_inp)
    rate = float(rate_inp)
except ValueError:
    print("Invalid input, please enter numeric values.")
    exit()

result = computepay(hours, rate)
print("Pay:", result)
