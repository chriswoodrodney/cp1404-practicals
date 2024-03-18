"""
NAME:CHRISWOOD RODNEY OKWIIRI
FILE:PROGRAMMING LANGUAGES

"""


class ProgrammingLanguage:
    """Represents a programming language."""

    def __init__(self, name, typing, reflection, year):
        """Initialize a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if the programming language is dynamically typed, False otherwise."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return a string representation of the ProgrammingLanguage."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

# Example usage:
lang1 = ProgrammingLanguage("Python", "Dynamic", True, 1991)
lang2 = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
lang3 = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(lang1)

languages = [lang1, lang2, lang3]

print("\nThe dynamically typed languages are:")
for language in languages:
    if language.is_dynamic():
        print(language.name)
