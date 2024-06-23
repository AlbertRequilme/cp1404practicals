"""
Pseudocode:
get gifts and students
leftover_gifts = gifts - students
received_gifts = gifts - leftover_gifts
display received_gifts
display leftover_gifts
"""
# Gifts and Students
# number_of_gifts = int(input("How many gifts?: "))
# number_of_students = int(input("How many students? "))
# leftover_gifts = number_of_gifts - number_of_students
# if leftover_gifts < 0:
#     print("There's not enough gifts for every student! :(")
# else:
#     print(f"Each student receives 1 gift.")
#     print(f"There are/is {leftover_gifts} gift/s left.")

# GST
# GST = 0.09
# item_price = float(input("Item Price: "))
# has_GST = input("Does this item have GST? (y/n): ").lower()
# if has_GST == "y":
#     total_item_price = (item_price * GST) + item_price
#     print(f"Your total price with GST is: ${total_item_price:.2f}")
# elif has_GST == "n":
#     print(f"Your price without GST is: ${item_price:.2f}")
# else:
#     print("Invalid Input")

# Loops
# While Loop:
# maximum_number = int(input("Max number: "))
# count = 1
# while count <= maximum_number:
#     print(count)
#     count += 1

# For Loop:
# maximum_number = int(input("Max number: "))
# for i in range(1, maximum_number + 1):
#     print(i)

# While Loop for SECRET Number
# SECRET = 7
# get_number = int(input("Guess the Secret number between 1 - 10!: "))
# while get_number != SECRET:
#     print("Guess Again!")
#     get_number = int(input("Guess!: "))
# print("Awesome! You guessed correctly!")

# Input validation:
# username = input("Username: ").capitalize()
# while username == "":
#     print("Invalid Input")
#     username = input("Username: ").capitalize()
# salary = float(input("Salary: "))
# while salary <= 0:
#     print("Invaid Input")
#     salary = float(input("Salary: "))
# print(f"Your username is {username} and your Salary is ${salary:.2f}")

# Ages
# amount_of_ages = int(input("How many ages: "))
# total_age = 0
# for i in range(amount_of_ages):
#     age = int(input(f"Enter Age {i + 1}: "))
#     total_age += age
# average_age = total_age/amount_of_ages
# print(f"Total ages: {total_age}")
# print(f"Average age: {average_age:.0f}")


# print("This program will keep asking for your age until you type -1")
# count = 0
# total_age = 0
# age = int(input("Enter Age: "))
# while age != -1:
#     count += 1
#     total_age += age
#     age = int(input("Enter Age: "))
# average_age = total_age/count
# print(f"Total Age: {total_age}")
# print(f"Average Age: {average_age:.0f}")

# for i in range(1, 4):
#     for j in range(2, 10, 3):
#         print(i, "-", j + i)