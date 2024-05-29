def main():
    name = get_name()
    display_menu()
    choice = input(">>> ")
    while choice != "q":
        if choice == "h":
            print(f"Hello {name}")
            display_menu()
            choice = input(">>> ")
        elif choice == "g":
            print(f"Goodbye {name}")
            display_menu()
            choice = input(">>> ")
        else:
            print("Invalid choice")
            display_menu()
            choice = input(">>> ")
    print("Finished.")


def display_menu():
    print("(H)ello\n(G)oodbye\n(Q)uit")


def get_name():
    name = input("Enter name: ").lower()
    return name


main()
