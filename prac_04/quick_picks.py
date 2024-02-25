import random

# Constants
MIN_NUMBER = 1
MAX_NUMBER = 45
NUM_NUMBERS_PER_LINE = 6

# Function to generate a quick pick line
def generate_quick_pick():
    line = []
    while len(line) < NUM_NUMBERS_PER_LINE:
        num = random.randint(MIN_NUMBER, MAX_NUMBER)
        if num not in line:
            line.append(num)
            line.sort()
    return line

# Main program
def main():
    # Ask the user for the number of quick picks
    num_quick_picks = int(input("How many quick picks? "))

    # Generate and display the quick picks
    for _ in range(num_quick_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(map(str, quick_pick)))

if __name__ == "__main__":
    main()
