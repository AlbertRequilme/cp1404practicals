AMOUNT_OF_NUMBERS = 5


def main():
    """This function will test my stock knowledge on lists."""
    numbers = []
    append_to_list(numbers)
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / AMOUNT_OF_NUMBERS}")


def append_to_list(numbers):
    """This function will append to a list"""
    for number in range(0, AMOUNT_OF_NUMBERS):
        get_number = int(input("Number: "))
        numbers.append(get_number)


main()
