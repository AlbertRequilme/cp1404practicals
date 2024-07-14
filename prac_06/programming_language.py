class ProgrammingLanguage:
    """Represents a Programming Language"""

    def __init__(self, name="", dynamic="", reflection=False, year=0):
        """initialise the name, dynamic, reflection, and year of ProgrammingLanguage"""
        self.name = name
        self.dynamic = dynamic
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Returns True if Dynamic, else False"""
        return self.dynamic == "Dynamic"

    def __str__(self):
        """Returns the object as a proper string"""
        return f"{self.name}, {self.dynamic} Typing, Reflection={self.reflection}, First appeared in {self.year}"
