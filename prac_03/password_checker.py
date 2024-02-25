"""
24-cp1404
OKWIIRI CHRISWOOD RODNEY
password_checker
"""
# Constants
MIN_LENGTH = 5
MAX_LENGTH = 15
SPECIAL_CHARACTERS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

def get_password():
    """Get the password from the user."""
    password = input("Please enter a valid password\nYour password must be between "
                     f"{MIN_LENGTH} and {MAX_LENGTH} characters, and contain:\n"
                     "    1 or more uppercase characters\n"
                     "    1 or more lowercase characters\n"
                     "    1 or more numbers\n"
                     f"{'    and 1 or more special characters: ' + SPECIAL_CHARACTERS if SPECIAL_CHARACTERS_REQUIRED else ''}\n"
                     "> ")
    return password

def print_password_stars(password):
    """Print asterisks based on the length of the password."""
    print("*" * len(password))

def validate_password(password):
    """Validate the strength of the password."""
    # Initialize counters
    lowercase_count = 0
    uppercase_count = 0
    digit_count = 0
    special_char_count = 0

    # Check each character in the password
    for char in password:
        if char.islower():
            lowercase_count += 1
        elif char.isupper():
            uppercase_count += 1
        elif char.isdigit():
            digit_count += 1
        elif SPECIAL_CHARACTERS_REQUIRED and char in SPECIAL_CHARACTERS:
            special_char_count += 1

    # Check if password meets all criteria
    if (MIN_LENGTH <= len(password) <= MAX_LENGTH and
        lowercase_count >= 1 and
        uppercase_count >= 1 and
        digit_count >= 1 and
        (not SPECIAL_CHARACTERS_REQUIRED or special_char_count >= 1)):
        return True
    else:
        return False

def main():
    password = get_password()
    while not validate_password(password):
        print("Invalid password!")
        password = get_password()
    print(f"Your {len(password)} character password is valid: {password}")

if __name__ == "__main__":
    main()
