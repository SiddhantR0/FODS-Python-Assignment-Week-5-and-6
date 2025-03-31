'''
This program has a class Employees with various attribute. Takes employee details from the user
and then saves it in a csv file. This program has the feature that lets the user to see the list of
employees as well as their details.
'''

import csv

class Employee:
    def __init__(self, empid, name, address, contact_number, spouse_name, number_of_child, salary):
        self.empid = empid
        self.name = name
        self.address = address
        self.contact_number = contact_number
        self.spouse_name = spouse_name
        self.number_of_child = number_of_child
        self.salary = salary

    def to_list(self):
        return [self.empid, self.name, self.address, self.contact_number, self.spouse_name, self.number_of_child, self.salary]

def add_employee():
    employees = []
    while True:
        try:
            empid = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            address = input("Enter Address: ")
            contact_number = input("Enter Contact Number: ")
            spouse_name = input("Enter Spouse Name (or 'None' if not applicable): ")
            number_of_child = int(input("Enter Number of Children: "))
            salary = float(input("Enter Salary: "))

            employee = Employee(empid, name, address, contact_number, spouse_name, number_of_child, salary)
            employees.append(employee.to_list())

            more = input("Do you want to add another employee? (yes/no): ").strip().lower()
            if more != 'yes':
                break

        except ValueError:
            print("Invalid input! Please enter correct data types.")

    try:
        with open("question7employees.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(employees)
        print("Employee details successfully saved to question7employees.csv!")
    except Exception as e:
        print(f"Error saving to file: {e}")

def display_employees():
    try:
        with open("question7employees.csv", "r") as file:
            reader = csv.reader(file)
            employees = list(reader)
            
            if not employees:
                print("No employee data found.")
                return

            print("\nEmployee List:")
            print("{:<10} {:<20} {:<20} {:<15} {:<15} {:<10} {:<10}".format(
                "EmpID", "Name", "Address", "Contact No.", "Spouse", "Children", "Salary"))
            print("=" * 100)

            for emp in employees:
                print("{:<10} {:<20} {:<20} {:<15} {:<15} {:<10} {:<10}".format(*emp))

    except FileNotFoundError:
        print("No employee records found.")

while True:
    print("\nEmployee Management System")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Exit")

    choice = input("Enter your choice: ").strip()
    
    if choice == "1":
        add_employee()
    elif choice == "2":
        display_employees()
    elif choice == "3":
        print("Exiting program")
        break
    else:
        print("Invalid choice!")
