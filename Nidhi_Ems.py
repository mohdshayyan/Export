# importing mysql connector
import mysql.connector

# making Connection
con = mysql.connector.connect(
    host="localhost", user="root", password="root")


# Function to create database
def create_database():
    cursor = con.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ems")
    con.commit()

# Function to create tables
def create_tables():
    cursor = con.cursor()
    cursor.execute("USE ems")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS empd (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            post VARCHAR(255) NOT NULL,
            salary DECIMAL(10, 2) NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS workers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            position VARCHAR(255) NOT NULL,
            wage DECIMAL(10, 2) NOT NULL
        )
    """)
    con.commit()

# Function to Add_Employee
def Add_Employ():
    print("Select Employee Type:")
    print("1. Regular Employee")
    print("2. Worker")
    emp_type = int(input("Enter your choice: "))

    if emp_type == 1:
        Id = input("Enter Employee Id : ")
        Name = input("Enter Employee Name : ")
        Post = input("Enter Employee Post : ")
        Salary = input("Enter Employee Salary : ")
        data = (Id, Name, Post, Salary)

        # Inserting Employee details in
        # the Employee Table
        sql = 'insert into empd values(%s,%s,%s,%s)'
    elif emp_type == 2:
        Id = input("Enter Worker Id : ")
        Name = input("Enter Worker Name : ")
        Position = input("Enter Worker Position : ")
        Wage = input("Enter Worker Wage : ")
        data = (Id, Name, Position, Wage)

        # Inserting Worker details in
        # the Worker Table
        sql = 'insert into workers values(%s,%s,%s,%s)'
    else:
        print("Invalid choice.")
        return

    c = con.cursor()

    # Executing the SQL Query
    c.execute(sql, data)

    # commit() method to make changes in
    # the table
    con.commit()
    print("Employee/Worker Added Successfully ")
    menu()

# Function to Promote Employee
def Promote_Employee():
    Id = int(input("Enter Employee/Worker's Id"))

    # Checking if Employee/Worker with given Id
    # Exist or Not
    if not check_employee(Id):
        print("Employee/Worker does not exist\nTry Again\n")
        menu()
    else:
        Amount = int(input("Enter increase in Salary/Wage"))

        # Determine whether it's an employee or worker
        table_name = 'empd' if check_employee_type(Id) == 'empd' else 'workers'

        # Query to Fetch Salary/Wage of Employee/Worker
        # with given Id
        sql = f'select salary from {table_name} where id=%s'
        data = (Id,)
        c = con.cursor()

        # Executing the SQL Query
        c.execute(sql, data)

        # Fetching Salary/Wage of Employee/Worker with given Id
        r = c.fetchone()
        t = r[0] + Amount

        # Query to Update Salary/Wage of Employee/Worker with
        # given Id
        sql = f'update {table_name} set salary=%s where id=%s'
        d = (t, Id)

        # Executing the SQL Query
        c.execute(sql, d)

        # commit() method to make changes in the table
        con.commit()
        print("Employee/Worker Promoted")
        menu()

# Function to Remove Employee/Worker with given Id
def Remove_Employ():
    Id = input("Enter Employee/Worker Id : ")

    # Checking if Employee/Worker with given Id Exist
    # or Not
    if not check_employee(Id):
        print("Employee/Worker does not exist\nTry Again\n")
        menu()
    else:

        # Determine whether it's an employee or worker
        table_name = 'empd' if check_employee_type(Id) == 'empd' else 'workers'

        # Query to Delete Employee/Worker from Table
        sql = f'delete from {table_name} where id=%s'
        data = (Id,)
        c = con.cursor()

        # Executing the SQL Query
        c.execute(sql, data)

        # commit() method to make changes in
        # the table
        con.commit()
        print("Employee/Worker Removed")
        menu()

# Function To Check if Employee/Worker with
# given Id Exist or Not
def check_employee(employee_id):
    # Query to select all Rows from
    # employee/worker Table
    sql = 'select * from empd where id=%s'
    c = con.cursor(buffered=True)
    data = (employee_id,)
    c.execute(sql, data)

    # rowcount method to find
    # number of rows with given values
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False

# Function to Check the type of Employee/Worker
def check_employee_type(employee_id):
    # Query to select all Rows from
    # employee/worker Table
    sql = 'select * from empd where id=%s'
    c = con.cursor(buffered=True)
    data = (employee_id,)
    c.execute(sql, data)

    # rowcount method to find
    # number of rows with given values
    r = c.rowcount
    if r == 1:
        return 'empd'
    else:
        return 'workers'

# Function to Display All Employees
# from Employee Table
def Display_Employees():
    emp_sql = 'select * from empd'
    worker_sql = 'select * from workers'
    c = con.cursor()

    # Executing the SQL Query
    c.execute(emp_sql)
    r = c.fetchall()
    print("Employee Details:")
    for i in r:
        print("Employee Id : ", i[0])
        print("Employee Name : ", i[1])
        print("Employee Post : ", i[2])
        print("Employee Salary : ", i[3])

    # Executing the SQL Query
    c.execute(worker_sql)
    r = c.fetchall()
    print("\nWorker Details:")
    for i in r:
        print("Worker Id : ", i[0])
        print("Worker Name : ", i[1])
        print("Worker Position : ", i[2])
        print("Worker Wage : ", i[3])

    menu()

# menu function to display menu
def menu():
    print("----------------Modules in Employee Management System ---------")
    print("Press ")
    print("1 to Add Employee/Worker")
    print("2 to Remove Employee/Worker ")
    print("3 to Promote Employee/Worker")
    print("4 to Display Employees")
    print("5 to Exit")

    ch = int(input("Enter your Choice "))
    if ch == 1:
        Add_Employ()
    elif ch == 2:
        Remove_Employ()
    elif ch == 3:
        Promote_Employee()
    elif ch == 4:
        Display_Employees()
    elif ch == 5:
        exit(0)
    else:
        print("Invalid Choice")
        menu()

# Create database and tables
create_database()
create_tables()

# Calling menu function
menu()
