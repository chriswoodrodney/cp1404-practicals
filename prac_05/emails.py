"""
name: CHRISWOOD RODNEY OKWIIRI
file: email
"""
def extract_name(email):
    """
    Extracts the name from an email address.
    Assumes that the email format is 'firstname.lastname@domain.com'.
    """
    parts = email.split('@')[0].split('.')
    return ' '.join(part.title() for part in parts)

def main():
    email_dict = {}  # Initialize an empty dictionary to store emails and names

    while True:
        email = input("Email: ")
        if not email:  # If the user enters a blank email, exit the loop
            break

        name = extract_name(email)
        correct_name = input(f"Is your name {name}? (Y/n) ").strip().lower()

        if correct_name in ('', 'y'):
            email_dict[email] = name
        else:
            name = input("Name: ")
            email_dict[email] = name

    print("\nStored emails and names:")
    for email, name in email_dict.items():
        print(f"{name} ({email})")

if __name__ == "__main__":
    main()
""
