def main():
    """Display income report for incomes over a given number of months."""
    income_data = []
    num_months = int(input("How many months? "))

    for month in range(1, num_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        income_data.append(income)

    print("\nIncome Report\n-------------")
    print_report(income_data, num_months)


def print_report(incomes, num_months):
    """Print the income report."""
    total = 0
    for month in range(1, num_months + 1):
        income = incomes[month - 1]
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


if __name__ == "__main__":
    main()
