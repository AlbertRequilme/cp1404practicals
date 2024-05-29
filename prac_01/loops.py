def base():
    for i in range(1, 21, 2):
        print(i, end=' ')
    print()


def a():
    for i in range(0, 101, 10):
        print(i, end=' ')
    print()


def b():
    for i in range(20, 0, -1):
        print(i, end=' ')
    print()


def c():
    starcount = int(input("How many stars?: "))
    print(f"Number of stars: {starcount}")
    for i in range(1, starcount + 1):
        print("*", end='')
    print()


def d():
    starcount = int(input("How many stars?: "))
    for i in range(1, starcount + 1):
        for j in range(i):
            print("*", end='')
        print()


# base()
# a()
# b()
# c()
d()
