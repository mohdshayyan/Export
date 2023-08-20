import mysql.connector
import pandas as pd



# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

def create_database():
    cursor = db.cursor()
    cursor.execute('CREATE DATABASE IF NOT EXISTS employee_management')
    cursor.execute('USE employee_management')


# Create tables
    cursor.execute("CREATE TABLE Departments (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")
    cursor.execute("CREATE TABLE Positions (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255))")
    cursor.execute("CREATE TABLE Employees (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), department_id INT, position_id INT, FOREIGN KEY (department_id) REFERENCES Departments(id), FOREIGN KEY (position_id) REFERENCES Positions(id))")
create_database()

cursor = db.cursor()
# Insert data
departments = ['HR', 'Finance', 'IT']
for department in departments:
    cursor.execute("INSERT INTO Departments (name) VALUES (%s)", (department,))
db.commit()

positions = ['Manager', 'Developer', 'Analyst']
for position in positions:
    cursor.execute("INSERT INTO Positions (title) VALUES (%s)", (position,))
db.commit()

employees = [
    {'name': 'John Doe', 'department_id': 1, 'position_id': 1},
    {'name': 'Jane Smith', 'department_id': 2, 'position_id': 2},
    {'name': 'Michael Johnson', 'department_id': 3, 'position_id': 3}
]
for employee in employees:
    cursor.execute("INSERT INTO Employees (name, department_id, position_id) VALUES (%s, %s, %s)", (employee['name'], employee['department_id'], employee['position_id']))
db.commit()

# Retrieve data using lists, dictionaries, and dataframes
cursor.execute("SELECT * FROM Departments")
departments_data = cursor.fetchall()

departments_list = [department[1] for department in departments_data]
departments_dict = {department[0]: department[1] for department in departments_data}

cursor.execute("SELECT * FROM Employees")
employees_data = cursor.fetchall()

employees_list = [{'id': emp[0], 'name': emp[1], 'department_id': emp[2], 'position_id': emp[3]} for emp in employees_data]
employees_df = pd.DataFrame(employees_data, columns=['id', 'name', 'department_id', 'position_id'])

print("Departments List:", departments_list)
print("Departments Dictionary:", departments_dict)
print("Employees List:", employees_list)
print("Employees DataFrame:\n", employees_df)

# Close the database connection

db.close()


#

import matplotlib.pyplot as plt
#Prepare the data you want to visualize. For example, if you want to create a bar chart of the number of employees in each department, you can use the departments_data you fetched earlier:departments_names = [department[1] for department in departments_data]
employees_count = [len([emp for emp in employees_list if emp['department_id'] == department[0]]) for department in departments_data]#Create the visualization using Matplotlib. For example, to create a bar chart:plt.bar(departments_names, employees_count)
plt.xlabel('Departments')
plt.ylabel('Number of Employees')
plt.title('Employee Distribution by Department')
plt.xticks(rotation=45)
plt.show()#Similarly, you can create other types of visualizations like pie charts, line charts, scatter plots, etc. by using appropriate Matplotlib functions.Remember to add these Matplotlib-related code snippets after youve retrieved and processed your data but before you close the database connection.





