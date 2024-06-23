def main():
    number_of_items = get_valid_number("Number of items: ", 0)
    total_price = calculate_total_price(number_of_items)
    print(f"Total price for {number_of_items} items is ${total_price:.2f}")


def calculate_total_price(number_of_items):
    total_price = 0
    for i in range(number_of_items):
        price = float(input("Price of item: "))
        total_price += price
    if total_price > 100:
        total_price *= 0.9
    return total_price


def get_valid_number(prompt, low):
    number = int(input(prompt))
    while number < low:
        print("Invalid Number of Items!")
        number = int(input(prompt))
    return number


main()
