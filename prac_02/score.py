"""
CP1404 - week1
Name: Chriswood Rodney Okwiiri
broken_score
"""
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

def main():
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(result)

if __name__ == "__main__":
    main()
