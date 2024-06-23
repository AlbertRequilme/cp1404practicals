import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_LINE = 6


def main():
    number_of_picks = int(input("How many quick picks? "))
    generate_quick_picks(number_of_picks)


def generate_quick_picks(number_of_picks):
    for i in range(number_of_picks):
        quick_pick = generate_unique_numbers()
        quick_pick.sort()
        print(" ".join(f"{number:2}" for number in quick_pick))


def generate_unique_numbers():
    numbers = []
    while len(numbers) < NUMBERS_PER_LINE:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in numbers:
            numbers.append(number)
    return numbers


main()
