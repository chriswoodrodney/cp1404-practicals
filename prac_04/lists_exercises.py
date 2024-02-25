def main():
    # Prompt the user for 5 numbers
    numbers = [float(input(f"Number {i + 1}: ")) for i in range(5)]

    # Output information about the numbers
    print("The first number is", numbers[0])
    print("The last number is", numbers[-1])
    print("The smallest number is", min(numbers))
    print("The largest number is", max(numbers))
    print("The average of the numbers is", sum(numbers) / len(numbers))

if __name__ == "__main__":
    main()

# List of authorized usernames
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
             'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

# Ask the user for their username
username = input("Enter your username: ")

# Check if the username is in the list of authorized users
if username in usernames:
    print("Access granted")
else:
    print("Access denied")
