"""
CP1404/CP5632 Practical - Suggested Solution
Programming Language class with tests.
"""


class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name, typing, reflection, year, arithmetic):
        """Construct a ProgrammingLanguage from the given values."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.arithmetic = arithmetic

    def __repr__(self):
        """Return string representation of a ProgrammingLanguage."""
        return (f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}, "
                f"Supports Pointer Arithmetic = {self.arithmetic}")

    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"


def run_tests():
    """Run simple tests/demos on ProgrammingLanguage class."""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995, "Yes")
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991, "Yes")
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991, "Yes")

    languages = [ruby, python, visual_basic]
    print(python)

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    run_tests()
