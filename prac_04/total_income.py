"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {str(month)}: "))
        incomes.append(income)

    print("\nIncome Report\n-------------")
    print(print_report(incomes, number_of_months))


def print_report(incomes, number_of_months):
    """This function will print a report of X income over a set of Y months"""
    total = 0
    for month in range(1, number_of_months + 1):
        income = incomes[month - 1]
        total += income
        return f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}"


main()
