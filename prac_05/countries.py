import csv


def read_data(filename):
    countries = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for column in reader:
            country = column[0]
            city = column[1]
            population = int(column[2].replace(',', ''))
            growth = float(column[3].strip('%')) / 100
            countries[country] = (city, population, growth)
    return countries


def calculate_max_lengths(sorted_countries):
    max_country_len = max(len(country) for country in sorted_countries)
    max_city_len = max(len(country) for country in sorted_countries)
    max_population_len = max(len(f"{sorted_countries[country][1]:,}") for country in sorted_countries)
    return max_country_len, max_city_len, max_population_len


def print_formatted_output(sorted_countries, max_country_len, max_city_len, max_population_len):
    for country in sorted_countries:
        city, population, growth = sorted_countries[country]
        growth_rate = growth * 100
        print(
            f"{country:<{max_country_len}} - {city:<{max_city_len}} {population:<{max_population_len}}({growth_rate:.2f}%)")


def main():
    filename = 'countries.csv'
    data = read_data(filename)
    sorted_countries = dict(sorted(data.items()))
    max_lengths = calculate_max_lengths(sorted_countries)
    print_formatted_output(sorted_countries, *max_lengths)


main()
