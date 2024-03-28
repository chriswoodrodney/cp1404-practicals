class Project:
    def __init__(self, name="", start_date="", priority=0, cost_estimate=0.0, completion_percentage=0):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return f"{self.name}\t{self.start_date}\t{self.priority}\t{self.cost_estimate}\t{self.completion_percentage}"


def load_projects(file_name):
    projects = []
    with open(file_name, 'r') as file:
        for line in file:
            name, start_date, priority, cost_estimate, completion_percentage = line.strip().split('\t')
            priority = int(priority)
            cost_estimate = float(cost_estimate)
            completion_percentage = int(completion_percentage)
            projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
    return projects


def display_projects(projects):
    print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage")
    for project in projects:
        print(project)


def create_projects_file(file_name):
    with open(file_name, 'w') as file:
        file.write("Build Car Park\t12/09/2021\t2\t600000.0\t95\n")
        file.write("Mow Lawn\t31/10/2022\t3\t3.0\t0\n")
        file.write("Organise Pantry\t20/07/2022\t1\t25.0\t55\n")
        file.write("Record Music Video\t01/12/2022\t9\t250000.0\t0\n")
        file.write("Read 7 Habits Book\t13/12/2021\t6\t99.0\t100\n")


def main():
    projects_file = "projects.txt"
    create_projects_file(projects_file)
    projects = load_projects(projects_file)
    display_projects(projects)


if __name__ == "__main__":
    main()
