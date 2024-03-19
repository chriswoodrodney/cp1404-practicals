"""
NAME:CHRISWOOD RODNEY OKWIIRI
FILE:GUITARS
"""
from guitar import Guitar  # Import the Guitar class from the guitar module

def main():
    print("My guitars!")
    guitars = []


    while True:
        name = input("Name: ")
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:.2f} added.\n")


    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name} ({guitar.year}), worth ${guitar.cost:,.2f}{vintage_string}")

if __name__ == "__main__":
    main()