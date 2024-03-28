# programming_language.py
class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name, typing, reflection, year, pointer_arithmetic):
        """
        Construct a ProgrammingLanguage object.

        Parameters:
        - name (str): The name of the programming language.
        - typing (str): The typing discipline of the programming language.
        - reflection (bool): Indicates whether the language supports reflection.
        - year (int): The year the programming language was first released.
        - pointer_arithmetic (bool): Indicates whether the language supports pointer arithmetic.
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic

    def __repr__(self):
        """
        Return string representation of a ProgrammingLanguage object.

        Returns:
        - str: String representation of the object.
        """
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}, Pointer Arithmetic={self.pointer_arithmetic}"


# language_file_reader.py
import csv
from collections import namedtuple
from programming_language import ProgrammingLanguage


def main():
    """Read file of programming language details, save as objects, display."""
    languages = []
    # Open the file for reading
    with open('languages.csv', 'r') as in_file:
        reader = csv.reader(in_file)
        # Consume the header
        next(reader)
        # Read language data
        for row in reader:
            name, typing, reflection, year, pointer_arithmetic = row
            reflection = reflection == "Yes"
            pointer_arithmetic = pointer_arithmetic == "Yes"
            language = ProgrammingLanguage(name, typing, reflection, int(year), pointer_arithmetic)
            languages.append(language)

    # Loop through and display all languages (using their str method)
    for language in languages:
        print(language)


def using_namedtuple():
    """Language file reader version using a named tuple."""
    Language = namedtuple('Language', 'name, typing, reflection, year, pointer_arithmetic')
    with open('languages.csv', 'r') as in_file:
        reader = csv.reader(in_file)
        next(reader)  # Consume the header
        for row in reader:
            language = Language._make(row)
            print(repr(language))


def using_csv_namedtuple():
    """Language file reader version using both csv module and named tuple."""
    Language = namedtuple('Language', 'name, typing, reflection, year, pointer_arithmetic')
    with open("languages.csv", "r") as in_file:
        reader = csv.reader(in_file)
        next(reader)  # Consume the header
        for language in map(Language._make, reader):
            print(language.name, 'was released in', language.year)
            print(repr(language))


if __name__ == "__main__":
    main()
