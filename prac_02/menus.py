def determine_result(score):
    """Determine the result based on the score."""
    if 0 <= score <= 100:
        if score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Passable"
        else:
            return "Bad"
    else:
        return "Invalid score"

def print_result(score):
    """Print the result based on the score."""
    result = determine_result(score)
    print(f"Result: {result}")

def show_stars(score):
    """Print stars based on the score."""
    print("*" * int(score))

def get_valid_score():
    """Get a valid score from the user."""
    while True:
        try:
            score = float(input("Enter score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Score must be between 0 and 100 inclusive.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    score = get_valid_score()
    print("Initial score set.")

    while True:
        print("\nMENU:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")

        choice = input(">>> ").upper()

        if choice == "G":
            score = get_valid_score()
            print("Score updated.")
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            show_stars(score)
        elif choice == "Q":
            print("Thank you for using the program. Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
