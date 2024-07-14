class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Initialises name, year, cost, and age"""
        self.name = name
        self.year = year
        self.cost = cost
        self.age = 0

    def get_age(self):
        """Updates the age by subtracting the current year with its year made."""
        self.age = 2024 - self.year

    def is_vintage(self):
        """Determines if the guitar is vintage or not"""
        return self.age >= 50

    def __str__(self):
        """Returns with a proper string"""
        return f"{self.name:>10} ({self.year}), worth ${self.cost:.2f}"
