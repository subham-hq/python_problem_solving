"""
Solution for a Python practice exercise:
Repeatedly prompt the user for numbers until 'done' is entered.
Print the largest and smallest values. Ignore invalid inputs.
"""

largest = None
smallest = None

while True:
    num = input("Enter a number: ")

    if num.lower() == "done":
        break

    try:
        value = int(num)

        if largest is None or value > largest:
            largest = value

        if smallest is None or value < smallest:
            smallest = value

    except ValueError:
        print("Invalid input.")
        continue

print("Maximum is", largest)
print("Minimum is", smallest)
