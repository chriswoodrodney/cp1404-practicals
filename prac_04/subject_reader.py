def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    FILENAME = "data.txt"  # Placeholder value for FILENAME
    data = []
    with open(FILENAME) as input_file:
        for line in input_file:
            line = line.strip()
            parts = line.split(',')
            parts[2] = int(parts[2])
            data.append(parts)
    return data

def main():
    data = get_data()
    print(data)

if __name__ == "__main__":
    main()
