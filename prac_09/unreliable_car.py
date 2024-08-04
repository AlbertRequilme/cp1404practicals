from prac_09.car import Car
import random


class UnreliableCar(Car):
    """A car that is unreliable"""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance, based on Car"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drives the car, with a chance to fail based on reliability"""
        chance_to_drive = random.randint(0, 100)
        if chance_to_drive <= self.reliability:
            return super().drive(distance)
        else:
            return 0

    def __str__(self):
        """Return a string representation of UnreliableCar"""
        return f"{self.name}, fuel={self.fuel}, odometer={self._odometer}"
