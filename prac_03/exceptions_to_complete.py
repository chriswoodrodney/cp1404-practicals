"""
24-cp1404
OKWIIRI CHRISWOOD RODNEY
exceptions to complete
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        # TODO: Set is_finished to True to exit the loop when a valid integer is entered
        is_finished = True
    except ValueError:  # TODO - add the exception you want to catch after except
        print("Please enter a valid integer.")
print("Valid result is:", result)

