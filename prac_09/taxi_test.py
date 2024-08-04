from prac_09.taxi import Taxi


def main():
    """Demo test code to show how to use Taxi subclass."""
    my_taxi = Taxi("Prius 1", 100)
    my_taxi.drive(40)
    print(f"Current fare: ${my_taxi.get_fare()}")
    print(my_taxi)
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(f"Current fare: ${my_taxi.get_fare()}")
    print(my_taxi)


main()
