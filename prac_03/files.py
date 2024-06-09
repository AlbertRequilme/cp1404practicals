def number_1():
    out_file = open("name.txt", 'w')
    get_name = input("Name: ")
    print(get_name, file=out_file)
    out_file.close()


def number_2():
    read_file = open("name.txt", 'r')
    print(read_file.readline())
    read_file.close()


def number_3():
    with open("numbers.txt", 'r') as file:
        first_number = int(file.readline().strip())
        second_number = int(file.readline().strip())
    result = first_number + second_number
    print(result)


def number_4():
    total = 0
    with open("numbers.txt", 'r') as file:
        for line in file:
            number = int(line)
            total += number
        print(total)


# number_1()
# number_2()
# number_3()
number_4()