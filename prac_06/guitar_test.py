from prac_06.guitar import Guitar

gibson = Guitar("Gibson", 1922, 16035.40)
another_guitar = Guitar("test", 2013, 0)


def test():
    """This is a function used for testing"""
    gibson.get_age()
    print(gibson.age)
    # Gibson L - 5 CES get_age() - Expected 102. Got 102
    another_guitar.get_age()
    print(another_guitar.age)
    # Another Guitar get_age() - Expected 11. Got 11
    print(gibson.is_vintage())
    # Gibson L - 5 CES is_vintage() - Expected True.Got True
    print(another_guitar.is_vintage())
    # Another Guitar is_vintage() - Expected False.Got False


test()
