class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year})\nCost: ${self.cost:,.2f}"

    def get_age(self):
        current_year = 2022  # Assuming the current year is 2022
        return current_year - self.year

    def is_vintage(self):
        return self.get_age() >= 50


# Create a list to store multiple guitars
guitars = []

# Add guitars to the list
guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Fender Stratocaster", 1954, 1200.00))
guitars.append(Guitar("Martin D-28", 1968, 3500.00))
# Add more guitars as needed...

# Iterate over the list of guitars and print their details
for guitar in guitars:
    print(guitar)
    print("Age:", guitar.get_age())
    print("Is vintage?", guitar.is_vintage())
    print()
