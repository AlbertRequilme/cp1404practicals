from prac_09.unreliable_car import UnreliableCar


def main():
    """Demo test code to show how to use Taxi subclass."""
    my_strange_car = UnreliableCar("Honda Civic", 100, 50)
    my_strange_car.drive(20)
    print(my_strange_car)


def test1():
    """Testing the chance boundaries of reliability to see if it works"""
    test_car = UnreliableCar("Test1", 100, 100)
    test_car.drive(50)
    print(test_car)  # This should output a guaranteed chance to drive, with fuel=50 and odometer=50
    test_car2 = UnreliableCar("Test2", 100, 0)
    test_car2.drive(50)
    print(test_car2)  # This should output a guaranteed chance to fail, with fuel=100 and odometer=100


# test1()
main()
