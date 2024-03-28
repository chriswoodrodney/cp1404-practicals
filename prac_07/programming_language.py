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

    def __str__(self):
        """
        Return a formatted string representation of the ProgrammingLanguage object.

        Returns:
        - str: Formatted string representation.
        """
        return f"Programming Language: {self.name}\n" \
               f"Typing: {self.typing}\n" \
               f"Reflection: {'Yes' if self.reflection else 'No'}\n" \
               f"Year: {self.year}\n" \
               f"Pointer Arithmetic: {'Yes' if self.pointer_arithmetic else 'No'}"

    def is_dynamic(self):
        """
        Determine if the programming language is dynamically typed.

        Returns:
        - bool: True if dynamically typed, False otherwise.
        """
        return self.typing == "Dynamic"

    def supports_pointer_arithmetic(self):
        """
        Check if the programming language supports pointer arithmetic.

        Returns:
        - bool: True if supports pointer arithmetic, False otherwise.
        """
        return self.pointer_arithmetic


def run_tests():
    """Run simple tests/demos on ProgrammingLanguage class."""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995, False)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991, False)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991, False)

    languages = [ruby, python, visual_basic]
    print(python)

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

    print("\nThe languages supporting pointer arithmetic are:")
    for language in languages:
        if language.supports_pointer_arithmetic():
            print(language.name)


if __name__ == "__main__":
    run_tests()
