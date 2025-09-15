"""
Employee Management Console Application

Allows creating, listing, reading, updating, and deleting employee records.
Interacts with a backend repository defined in db.repo_sql_dict.
"""

from db import repo_sql_dict as repo


def create_employee():
    """Handles creating a new employee via user input."""
    try:
        emp_id = int(input('ID: '))
        name = input('Name: ')
        age = int(input('Age: '))
        salary = float(input('Salary: '))
        is_active = input('Active (y/n): ').strip().upper() == 'Y'

        employee = {
            'id': emp_id,
            'name': name,
            'age': age,
            'salary': salary,
            'is_active': is_active
        }

        repo.create_employee(employee)
        print('Employee created successfully.')

    except ValueError:
        print('Invalid input. ID, Age, and Salary must be numbers.')
    except repo.EmployeeAlreadyExistError as ex:
        print(f"Error: {ex}")
    except repo.DatabaseError as ex:
        print(f"Database error: {ex}")


def list_employees():
    """Displays all employees."""
    print('List of Employees:')
    for employee in repo.read_all_employee():
        print(employee)


def read_employee():
    """Displays a single employee by ID."""
    try:
        emp_id = int(input('ID: '))
        employee = repo.read_by_id(emp_id)
        if employee is None:
            print('Employee not found.')
        else:
            print(employee)
    except ValueError:
        print('Invalid ID input.')


def update_employee():
    """Updates an employee's salary."""
    try:
        emp_id = int(input('ID: '))
        employee = repo.read_by_id(emp_id)

        if employee is None:
            print('Employee not found.')
            return

        print(employee)
        new_salary = float(input('New Salary: '))
        updated_employee = {
            'id': employee['id'],
            'name': employee['name'],
            'age': employee['age'],
            'salary': new_salary,
            'is_active': employee['is_active']
        }

        repo.update(emp_id, updated_employee)
        print('Employee updated successfully.')

    except ValueError:
        print('Invalid input. Salary and ID must be numbers.')


def delete_employee():
    """Deletes an employee by ID."""
    try:
        emp_id = int(input('ID: '))
        employee = repo.read_by_id(emp_id)

        if employee is None:
            print('Employee not found.')
        else:
            repo.delete_employee(emp_id)
            print('Employee deleted successfully.')

    except ValueError:
        print('Invalid ID input.')


def menu():
    """
    Display the menu and execute selected option.

    Returns:
        int: The user's selected menu option
    """
    message = '''
Options are:
1 - Create Employee
2 - List All Employees
3 - Read Employee By Id
4 - Update Employee
5 - Delete Employee
6 - Exit 
Your Option: '''

    try:
        choice = int(input(message))
    except ValueError:
        print('Invalid choice. Please enter a number between 1 and 6.')
        return 0

    if choice == 1:
        create_employee()
    elif choice == 2:
        list_employees()
    elif choice == 3:
        read_employee()
    elif choice == 4:
        update_employee()
    elif choice == 5:
        delete_employee()
    elif choice == 6:
        print('Thank you for using the application.')
    else:
        print('Invalid choice. Please enter a number between 1 and 6.')

    return choice


def menus():
    """Main loop to repeatedly show the menu until user exits."""
    user_choice = 0
    while user_choice != 6:
        user_choice = menu()


if __name__ == '__main__':
    menus()
