def do_this_now_1():
    """This gets a file name from the user and only prints lines that start with '#' """
    get_filename = input("Input Filename: ")
    open_file = open(f"{get_filename}", 'r')
    for line in open_file:
        if line.startswith('#'):
            print(line)
    open_file.close()
# Notes: Use readlines() to read line by line (only for removing specific lines)
# Use For loops to read many lines.


def do_this_now_2():
    s = "\tPython, Monty\n"
    print(s)
    print(s[1], ".", sep="")
    print(s.strip(), ".", sep="")
    s = s.replace(' ', '*')
    print(s)
    print(s.lstrip(),".", sep="")
    print(s.strip().split(','))


def do_this_now_3():
    name = input("Name: ")
    with open('name.txt', 'w') as out_file:
        print(name, file=out_file)
# This is the start of using "with x" as with allows you to open files without having to type .close()

def validate_input():
    age = 0
    valid_input = False
    while not valid_input:
        try:
            age = int(input("Age: "))
            valid_input = True
        except ValueError:
            print("Invalid input (Not an integer)")
        else:
            print(f"Next year you will be {age + 1}.")
        finally:
            print("Good Try.")


def do_this_now_4():
    is_finished = False
    result = 0
    while not is_finished:
        try:
            result = int(input("Enter a valid integer: "))
            is_finished = True
        except ValueError:
            print("An error occurred (Invalid Integer).")
    print("Valid result is:", result)


def do_this_now_5():
    try:
        value = int(input("> "))
        result = f"{value}" * value
        print(result)
    except TypeError:
        print("Invalid Calculation")


# whats_wrong_with_the_demo_in_video_1():




# do_this_now_1()
# do_this_now_2()
# do_this_now_3()
# do_this_now_4()
# do_this_now_5()
# validate_input()