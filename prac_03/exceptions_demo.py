"""
24-cp1404
OKWIIRI CHRISWOOD RODNEY
exceptions demo

Questions
1.When will a ValueError occur?
# will occur when the user inputs a value that cannot be converted to an integer, such as entering a string instead of a number.

2.When will a ZeroDivisionError occur?
# will occur when the user inputs 0 as the denominator, leading to division by zero, which is mathematically undefined.

3.Could you change the code to avoid the possibility of a ZeroDivisionError?
# yes
If you could figure out the answer to question 3, then make this change now.
"""
try:
    numerator = int(input("Enter the numerator: "))  # ValueError may occur if the input is not a valid integer
    denominator = int(input("Enter the denominator: "))  # ValueError may occur if the input is not a valid integer
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
