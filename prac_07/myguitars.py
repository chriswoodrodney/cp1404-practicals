class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name},{self.year},{self.cost}"

    def get_age(self, current_year):
        return current_year - self.year

    def is_vintage(self, current_year):
        return self.get_age(current_year) >= 50


def load_guitars(file_name):
    guitars = []
    with open(file_name, 'r') as file:
        for line in file:
            name, year, cost = line.strip().split(',')
            year = int(year)
            cost = float(cost)
            guitars.append(Guitar(name, year, cost))
    return guitars


def display_guitars(guitars, current_year):
    print("Guitars:")
    for i, guitar in enumerate(guitars, 1):
        print(f"{i}. {guitar} - Age: {guitar.get_age(current_year)}, Vintage: {guitar.is_vintage(current_year)}")
    print()


def add_guitar():
    name = input("Enter guitar name: ")
    year = int(input("Enter year built: "))
    cost = float(input("Enter cost: "))
    return Guitar(name, year, cost)


def main():
    current_year = 2022  # Assuming the current year is 2022
    guitars = load_guitars("guitars.csv")

    guitars.sort(key=lambda x: x.year)
    display_guitars(guitars, current_year)

    add_another = input("Do you want to add a new guitar? (yes/no): ").lower()
    while add_another == "yes":
        new_guitar = add_guitar()
        guitars.append(new_guitar)
        add_another = input("Do you want to add another guitar? (yes/no): ").lower()

    with open("guitars.csv", 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar}\n")

    print("All guitars have been written to 'guitars.csv'.")
    display_guitars(guitars, current_year)


if __name__ == "__main__":
    main()
