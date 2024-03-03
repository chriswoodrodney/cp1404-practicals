"""
name: CHRISWOOD RODNEY OKWIIRI
file: state_names
task: reformating
"""

# Reformatting code for PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

state_code = input("Enter short state: ")
while state_code != "":
    state_code = state_code.upper()  # Convert input to uppercase
    try:
        print(state_code, "is", CODE_TO_NAME[state_code])
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ")

# Loop to print all states and names neatly lined up
for code, name in CODE_TO_NAME.items():
    print(f"{code:<3} is {name}")
