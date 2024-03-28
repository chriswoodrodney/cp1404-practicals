import datetime

class Project:
    def __init__(self, name="", start_date="", priority=0, cost_estimate=0.0, completion_percentage=0):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, " \
               f"estimate: ${self.cost_estimate:,.2f}, completion: {self.completion_percentage}%"

    def __lt__(self, other):
        return self.priority < other.priority


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


def save_projects(file_name, projects):
    with open(file_name, 'w') as file:
        for project in projects:
            file.write(f"{project.name}\t{project.start_date}\t{project.priority}\t"
                       f"{project.cost_estimate}\t{project.completion_percentage}\n")


def display_projects(projects):
    incomplete_projects = [project for project in projects if project.completion_percentage < 100]
    completed_projects = [project for project in projects if project.completion_percentage == 100]

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")

    print("Completed projects:")
    for project in completed_projects:
        print(f"  {project}")


def filter_projects_by_date(projects):
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        filtered_projects = [project for project in projects if
                             datetime.datetime.strptime(project.start_date, "%d/%m/%Y").date() > filter_date]
        display_projects(filtered_projects)
    except ValueError:
        print("Invalid date format. Please use the format dd/mm/yyyy.")


def add_new_project(projects):
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))

    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)


def update_project(projects):
    display_projects(projects)
    try:
        index = int(input("Project choice: "))
        project = projects[index]
        print(project)
        new_completion_percentage = input("New Percentage: ")
        if new_completion_percentage:
            project.completion_percentage = int(new_completion_percentage)
        new_priority = input("New Priority: ")
        if new_priority:
            project.priority = int(new_priority)
    except (ValueError, IndexError):
        print("Invalid project choice.")


def main():
    projects_file = "projects.txt"
    projects = load_projects(projects_file)
    print(f"Welcome to Pythonic Project Management\nLoaded {len(projects)} projects from {projects_file}")

    while True:
        print("\n- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")
        choice = input(">>> ").lower()

        if choice == 'l':
            file_name = input("Enter filename to load projects from: ")
            projects = load_projects(file_name)
        elif choice == 's':
            file_name = input("Enter filename to save projects to: ")
            save_projects(file_name, projects)
            print(f"Projects saved to {file_name}")
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            save_prompt = input("Would you like to save to projects.txt? ").lower()
            if save_prompt.startswith('y'):
                save_projects(projects_file, projects)
                print(f"Projects saved to {projects_file}")
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice. Please choose from the menu options.")


if __name__ == "__main__":
    main()
