def main():
    get_password = input("Input Password: ")
    length_of_password = len(get_password)
    while length_of_password < 4:
        print("Invalid Length")
        get_password = input("Input Password: ")
        length_of_password = len(get_password)
    stars = "*" * length_of_password
    print(f"Your password is: {stars}")


main()
