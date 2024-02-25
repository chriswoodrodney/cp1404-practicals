def get_password():
    """Get the password from the user."""
    password = input("Enter your password: ")
    return password

def print_password_stars(password):
    """Print asterisks based on the length of the password."""
    print("*" * len(password))

def main():
    password = get_password()
    print_password_stars(password)

if __name__ == "__main__":
    main()
