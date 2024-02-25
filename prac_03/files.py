"""
24-cp1404
OKWIIRI CHRISWOOD RODNEY
files 1-4
"""
# 1. Write the user's name to a file
def write_name_to_file():
    name = input("Enter your name: ")
    with open("name.txt", "w") as file:
        file.write(name)

# 2. Read the name from the file and print it
def read_name_from_file():
    with open("name.txt", "r") as file:
        name = file.read().strip()
        print(f"Your name is {name}")

# 3. Read the first two numbers from "numbers.txt" and print their sum
def read_first_two_numbers():
    with open("numbers.txt", "r") as file:
        numbers = file.readlines()
        total = int(numbers[0]) + int(numbers[1])
        print("Sum of the first two numbers:", total)

# 4. Read all numbers from "numbers.txt" and print their total
def read_all_numbers():
    with open("numbers.txt", "r") as file:
        total = 0
        for line in file:
            total += int(line.strip())
        print("Total of all numbers:", total)

def main():
    # Task 1: Write the user's name to a file
    write_name_to_file()

    # Task 2: Read the name from the file and print it
    read_name_from_file()

    # Task 3: Read the first two numbers from "numbers.txt" and print their sum
    read_first_two_numbers()

    # Task 4: Read all numbers from "numbers.txt" and print their total
    read_all_numbers()

if __name__ == "__main__":
    main()



