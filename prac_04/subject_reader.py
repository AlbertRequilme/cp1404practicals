"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data2()
    display_data(data)


def load_data2():
    """This function will load the data within a list, using nested lists."""
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer
        data.append(parts)  # Add the parts to the data list
    input_file.close()
    return data


def display_data(data):
    """This function will display data in a nicer way."""
    for subject in data:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")


def test():
    """Using this function to test code."""
    data = load_data2()
    print(data)
    display_data(data)


main()
# test()
