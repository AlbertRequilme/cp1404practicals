import csv


def main():
    """This function does the loading and displaying of data"""
    filename = "wimbledon.csv"
    data = load_data(filename)
    champions = counts_wins_of_champion(data)
    countries = get_countries(data)
    display_champions(champions)
    display_countries(countries)


def load_data(filename):
    """This function reads the fils and returns it as a list of lists"""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        data = [line.strip().split(",") for line in in_file]
    return data


def counts_wins_of_champion(data):
    """This function will count the wins of each champions"""
    champions = {}
    for row in data:
        champion = row[2]
        if champion in champions:
            champions[champion] += 1
        else:
            champions[champion] = 1
    return champions


def get_countries(data):
    """This function simply sorts the countries"""
    countries = {row[1] for row in data}
    return sorted(countries)


def display_champions(champions):
    """This function displays the champions and their win counts"""
    print("Wimbledon Champions:")
    for champion, wins in sorted(champions.items()):
        print(f"{champion} {wins}")


def display_countries(countries):
    """This function displays the countries of the winners"""
    print("\nThese {} countries have won Wimbledon:".format(len(countries)))
    print(", ".join(countries))


main()
