import random


def main():
    score = float(input("Enter score: "))
    print(check_score(score))
    print("Randomly Generated Score: ")
    randomly_generated_score = generate_random_score()
    print(randomly_generated_score)
    print(check_score(randomly_generated_score))


def check_score(score):
    if score < 0 or score > 100:
        return "Invalid Score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    if score < 50:
        return "Bad"


def generate_random_score():
    random_score = random.randint(0, 100)
    return random_score


main()
