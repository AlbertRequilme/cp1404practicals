import csv
from prac_07.guitar import Guitar


def main():
    """This function will showcase a list of guitars, which the user can add upon"""
    filename = 'guitars.csv'
    guitars = read_guitars_from_file(filename)
    print("My Guitars!\nEnter none once you're done!")
    guitars.sort()  # This will sort by year using the __lt__ method
    display_guitars(guitars)
    print("Add a guitar if you wish to")
    name = input("Name: ").capitalize()
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        print(f"{name} ({year}) : ${cost:.2f} added.")
        guitars.append(Guitar(f"{name}", year, cost))
        name = input("Name: ").capitalize()
    print("These are my guitars:")
    guitars.sort()
    display_guitars(guitars)
    print("Guitars are awesome yo!")
    write_guitars_to_file(guitars, filename)


def read_guitars_from_file(filename):
    """This function will read the csv file inputted"""
    guitars = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row:
                name, year, cost = row
                guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def display_guitars(guitars):
    """This function will display the guitars"""
    for i, guitar in enumerate(guitars, 1):
        guitar.get_age()
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar} {vintage_string}")


def write_guitars_to_file(guitars, filename):
    """This function will write any guitars inputted by the user to a csv file"""
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


main()
