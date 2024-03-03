"""
name: CHRISWOOD RODNEY OKWIIRI
file: wimbledon
"""

def read_data(filename):
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)  # Skip header
        data = [line.strip().split(",") for line in in_file]
    return data

def count_champions(data):
    champions = {}
    for row in data:
        champion = row[2]
        champions[champion] = champions.get(champion, 0) + 1
    return champions

def get_countries(data):
    countries = set()
    for row in data:
        countries.add(row[1])
        countries.add(row[3])
    return sorted(countries)

def main():
    filename = "wimbledon_champions.csv"
    data = read_data(filename)
    champions = count_champions(data)
    countries = get_countries(data)

    print("Wimbledon Champions:")
    for champion, wins in sorted(champions.items()):
        print(f"{champion}: {wins}")

    print("\nThese", len(countries), "countries have won Wimbledon:")
    print(", ".join(countries))

if __name__ == "__main__":
    main()
