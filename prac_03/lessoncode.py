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


do_this_now_1()