employees = {}
last_id = 0  

def add_employee(name, job, salary):
    global last_id
    last_id += 1
    emp_id = last_id
    employees[emp_id] = {'name': name, 'job': job, 'salary': salary}
    print(f"Employee added with ID: {emp_id} and name: {name} with salary {salary}")

def print_employee_data(emp_id):
    if emp_id in employees:
        emp_info = employees[emp_id]
        print(f"Employee ID: {emp_id}")
        print(f"Name: {emp_info['name']}")
        print(f"Job: {emp_info['job']}")
        print(f"Salary: {emp_info['salary']}")
    else:
        print(f"Employee with ID {emp_id} does not exist.")

def remove_employee(emp_id):
    if emp_id in employees:
        del employees[emp_id]
        print(f"Employee with ID {emp_id} removed.")
    else:
        print(f"Employee with ID {emp_id} does not exist.")

def update_employee(emp_id, name=None, job=None, salary=None):
    if emp_id in employees:
        if name:
            employees[emp_id]['name'] = name
        if job:
            employees[emp_id]['job'] = job
        if salary:
            employees[emp_id]['salary'] = salary
        print(f"Employee with ID {emp_id} updated.")
    else:
        print(f"Employee with ID {emp_id} does not exist.")

def main():
    while True:
        print("\nEmployee Database Management System")
        print("1. Add new employee")
        print("2. Print employee data")
        print("3. Remove employee")
        print("4. Update employee")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter employee name: ")
            job = input("Enter employee job: ")
            salary = float(input("Enter employee salary: "))
            add_employee(name, job, salary)

        elif choice == '2':
            emp_id = int(input("Enter employee ID to print data: "))
            print_employee_data(emp_id)

        elif choice == '3':
            emp_id = int(input("Enter employee ID to remove: "))
            remove_employee(emp_id)

        elif choice == '4':
            emp_id = int(input("Enter employee ID to update: "))
            name = input("Enter new name (leave blank to keep current): ")
            job = input("Enter new job (leave blank to keep current): ")
            salary_str = input("Enter new salary (leave blank to keep current): ")
            salary = float(salary_str) if salary_str else None
            update_employee(emp_id, name, job, salary)

        elif choice == '5':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


main()
