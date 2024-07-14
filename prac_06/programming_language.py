class ProgrammingLanguage:
    """A way to choose your programming language"""

    def __init__(self, name="", dynamic="", reflection=False, year=0):
        self.name = name
        self.dynamic = dynamic
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.dynamic == "Dynamic"

    def __str__(self):
        return f"{self.name}, {self.dynamic} Typing, Reflection={self.reflection}, First appeared in {self.year}"
