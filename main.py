# Manually create a list of dictionaries to represent the dataset
employee_data = [
    {"Employee ID": 101, "Employee Name": "John Doe", "Department": "IT", "Salary": 55000.0, "Years of Experience": 5},
    {"Employee ID": 102, "Employee Name": "Jane Smith", "Department": "HR", "Salary": 60000.0, "Years of Experience": 8},
    {"Employee ID": 103, "Employee Name": "Alice Johnson", "Department": "IT", "Salary": 70000.0, "Years of Experience": 12},
    {"Employee ID": 104, "Employee Name": "Bob Brown", "Department": "Finance", "Salary": 75000.0, "Years of Experience": 15},
    # Add more employee data as needed
]

# Function to display employee information based on Employee ID
def display_employee_info(employee_id):
    for employee in employee_data:
        if employee["Employee ID"] == employee_id:
            print("Employee ID:", employee["Employee ID"])
            print("Employee Name:", employee["Employee Name"])
            print("Department:", employee["Department"])
            print("Salary:", employee["Salary"])
            print("Years of Experience:", employee["Years of Experience"])
            return
    print("Employee ID not found.")

# Algorithm 1: Calculate and display the average salary of all employees
def calculate_average_salary():
    total_salary = sum(employee["Salary"] for employee in employee_data)
    average_salary = total_salary / len(employee_data)
    print("Average Salary of All Employees:", average_salary)

# Algorithm 2: Display salary distribution for each department
def department_wise_salary_distribution():
    department_salaries = {}
    department_employee_count = {}
    
    for employee in employee_data:
        department = employee["Department"]
        if department in department_salaries:
            department_salaries[department] += employee["Salary"]
            department_employee_count[department] += 1
        else:
            department_salaries[department] = employee["Salary"]
            department_employee_count[department] = 1
    
    for department, total_salary in department_salaries.items():
        average_salary = total_salary / department_employee_count[department]
        print("Department:", department)
        print("Total Employees:", department_employee_count[department])
        print("Average Salary:", average_salary)
        print()

# Function to identify employees with more than 10 years of experience
def identify_high_experience_employees():
    high_experience_employees = []
    for employee in employee_data:
        if employee["Years of Experience"] > 10:
            high_experience_employees.append((employee["Employee Name"], employee["Department"]))
    if high_experience_employees:
        print("High Experience Employees:")
        for employee in high_experience_employees:
            print("Employee Name:", employee[0])
            print("Department:", employee[1])
    else:
        print("No high experience employees found.")

# Function to update employee salary based on Employee ID
def update_employee_salary(employee_id, new_salary):
    for employee in employee_data:
        if employee["Employee ID"] == employee_id:
            employee["Salary"] = new_salary
            print("Salary updated successfully for Employee ID:", employee_id)
            return
    print("Employee ID not found.")

# Main program loop
while True:
    print("\n===== Menu =====")
    print("1. Display Employee Information")
    print("2. Calculate Average Salary")
    print("3. Department-wise Salary Distribution")
    print("4. Identify High Experience Employees")
    print("5. Update Employee Salary")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        emp_id = int(input("Enter Employee ID: "))
        display_employee_info(emp_id)
    elif choice == '2':
        calculate_average_salary()
    elif choice == '3':
        department_wise_salary_distribution()
    elif choice == '4':
        identify_high_experience_employees()
    elif choice == '5':
        emp_id = int(input("Enter Employee ID: "))
        new_salary = float(input("Enter new salary: "))
        update_employee_salary(emp_id, new_salary)
    elif choice == '6':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please choose again.")
