emp_data = {}

def add_menu():
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Search for Employee")
    print("4. Exit")


def add_employee(emp_id,name,age,dept,salary):
    if emp_id in emp_data:
        print("Employee already exist")
        return
    else:
        emp_data[emp_id] = {
        'name' : name,
        'age' : age,
        'dept' : dept,
        'salary' : salary
        }
        print("Employee Added Succesfully")


def search_employee(emp_id):
    if emp_id in emp_data:
        emp = emp_data[emp_id]
        print(f"Name: {emp['name']}")
        print(f"Age: {emp['age']}")
        print(f"Department: {emp['dept']}")
        print(f"Salary: {emp['salary']}")
    else:
        print("Employee not found.")


def view_employee():
    if not emp_data:
        print("No employees found.")
    else:
        for emp_id, details in emp_data.items():
            print(f"\nEmployee ID: {emp_id}")
            print(f"Name: {details['name']}")
            print(f"Age: {details['age']}")
            print(f"Department: {details['dept']}")
            print(f"Salary: {details['salary']}")

while(True):
    add_menu()

    user_input = int(input("Enter you choice: "))

    if(user_input == 1):
        emp_id = int(input("Enter Employee id: "))
        name = input("Enter Employee name: ")
        age = int(input("Enter Employee age: "))
        dept = input("Enter the department name: ")
        salary = int(input("Enter Employee salary: "))


        add_employee(emp_id,name,age,dept,salary)

    elif user_input == 2:
        view_employee()

    elif(user_input == 3):
        emp_id = int(input("Enter Employee id: "))

        search_employee(emp_id)

    elif(user_input == 4):
        break

