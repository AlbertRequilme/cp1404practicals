"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
- When the input isn't a number
2. When will a ZeroDivisionError occur?
- When you divide by zero
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
- We can't change Zero division, but we can add a while loop to ask them again.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")