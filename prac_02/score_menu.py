def main():
    score = get_valid_number("Input a valid score: ", 0, 100)
    display_menu()
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "g":
            score = get_valid_number("Input a valid score: ", 0, 100)
            display_menu()
            choice = input(">>> ").lower()
        elif choice == "p":
            print(check_score(score))
            display_menu()
            choice = input(">>> ").lower()
        elif choice == "s":
            print("*" * score)
            display_menu()
            choice = input(">>> ").lower()
        else:
            print("Invalid choice")
            display_menu()
            choice = input(">>> ").lower()
    print("Farewell!")


def display_menu():
    print("(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit")


def check_score(score):
    if score < 0 or score > 100:
        return "Invalid Score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    if score < 50:
        return "Bad"


def get_valid_number(prompt, low, high):
    number = int(input(prompt))
    while number < low or number > high:
        print("Invalid Input.")
        number = int(input(prompt))
    return number


main()