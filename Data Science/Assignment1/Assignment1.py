import pandas as pd
## Employee management structure
employee = {
    101:{
        "name":"Satya",
        "age":27,
        "department":"HR",
        "salary":50000
    }
}

def add_employee():
    emp_id = int(input("Enter Employee ID:"))
    name = input("Enter Employee Name:")
    age = input("Enter Employee Age:")
    department = input("Enter Employee Department:")
    salary = input("Enter Employee Salary:")
    if emp_id in employee.keys():
        print("Employee ID already exists. Please Try again ! ! !")
        add_employee()
    else:
        employee[emp_id] = {
        "name":name,
        "age":age,
        "department":department,
        "salary":salary
        }
        print("Employee Details added ! ! !")

def view_employees():
    if len(employee)==0:
        print("No employees available.")
    else:
        df = pd.DataFrame.from_dict(employee, orient='index')
        df.index.name = 'employee_id'
        print(df)

def search_employee():
    emp_id = int(input("Enter Employee ID:"))
    details = employee.get(emp_id)
    if details:
        print("name : ",details["name"])
        print("age : ",details["age"])
        print("department : ",details["department"])
        print("salary : ",details["salary"])
    else:
        print("Employee not found.")

def main_menu():
    while True:
        print("\nChoose the Option from menu below:")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")
        choice = int(input("Enter your choice:"))
        if choice==1:
            add_employee()
        elif choice==2:
            view_employees()
        elif choice==3:
            search_employee()
        elif choice==4:
            print("Thank you for using this program")
            exit()
        else:
            print("Invalid Choice ! ! !  Please choose again.")

if __name__ == "__main__":
    main_menu()
