# What values do the following expressions have?
# numbers[0] -> 3
# numbers[-1] -> 2
# numbers[3] -> 1
# numbers[:-1] -> [3, 1, 4, 1, 5, 9]
# numbers[3:4] -> [1]
# 5 in numbers -> True
# 7 in numbers -> False
# "3" in numbers -> False (because "3" is a string, not an integer)
# numbers + [6, 5, 3] -> [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# In the same Python file, write statements to achieve the following:

numbers = [3, 1, 4, 1, 5, 9, 2]
numbers[0] = "ten"  # Change the first element of numbers to "ten"
numbers[-1] = 1  # Change the last element of numbers to 1
print(numbers[2:])  # Print all the elements from numbers except the first two (slice)
print(9 in numbers)  # Print whether 9 is an element of numbers
