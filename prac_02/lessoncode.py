# import random
#
# get_min_number = int(input("Input your Low Number: "))
# get_max_number = int(input("Input your High Number:"))
# while get_max_number <= get_min_number:
#     print("Invalid Input")
#     get_max_number = int(input("Input your High Number:"))
# n = random.randint(get_min_number, get_max_number)
# print(n * ":)")

import random


def main():
    name = get_valid_name()
    display_menu()
    choice = input(">>> ").lower()
    secret_list = ["Help", "Me", "Hi", "Hello"]
    while choice != "q":
        if choice == "h":
            print(f"Hello {name}!")
            display_menu()
            choice = input(">>> ").lower()
        elif choice == "g":
            print(f"Goodbye {name}.")
            display_menu()
            choice = input(">>> ").lower()
        elif choice == "s":
            print(f"{secret_list[return_random_number()]}")
            display_menu()
            choice = input(">>> ").lower()
        else:
            print("Invalid input")
            display_menu()
            choice = input(">>> ").lower()
    print("Program End")


def get_valid_name():
    name = input("Enter your name: ")
    while name == "":
        print("Invalid Name")
        name = input("Enter your name: ")
    return name


def display_menu():
    print("(H)ello\n(G)oodbye\n(S)ecret\n(Q)uit")


def return_random_number():
    return random.randint(0, 3)


main()
