from prac_06.guitar import Guitar


def main():
    """This function will ask for a guitar and then display them after entering a blank name."""
    guitars = []
    print("My Guitars!")
    name = input("Name: ").capitalize()
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        print(f"{name} ({year}) : ${cost:.2f} added.")
        guitars.append(Guitar(f"{name}", year, cost))
        name = input("Name: ").capitalize()
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        guitar.get_age()
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar} {vintage_string}")
    print("Guitars are awesome yo!")


main()
