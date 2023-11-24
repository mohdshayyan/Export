import mysql.connector

# Connecting to the MySQL server
mydb = mysql.connector.connect(
    host="localhost",
    user='root',
    password='root'
)

# Creating a database
def create_database():
    cursor = mydb.cursor()
    cursor.execute('CREATE DATABASE IF NOT EXISTS Hosp')
    cursor.execute('USE Hosp')

# Creating Patients table
def create_patients_table():
    cursor = mydb.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Patients (Id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT, gender VARCHAR(10), contact VARCHAR(15))')

# Creating Doctors table
def create_doctors_table():
    cursor = mydb.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Doctors (Id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), specialization VARCHAR(255), contact VARCHAR(15))')

# Creating Appointments table
def create_appointments_table():
    cursor = mydb.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Appointments (Id INT AUTO_INCREMENT PRIMARY KEY, patient_id INT, doctor_id INT, date DATE, time VARCHAR(255))')

# Define the function to add a new patient
def add_patient():
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    gender = input("Enter patient gender: ")
    contact = input("Enter patient contact number: ")
    cursor = mydb.cursor()
    sql = "INSERT INTO Patients (name, age, gender, contact) VALUES (%s, %s, %s, %s)"
    val = (name, age, gender, contact)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) inserted.")

# Define the function to view patient details
def view_patients():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Patients")
    result = cursor.fetchall()
    for row in result:
        print(row)

# Define the function to update patient details
def update_patient():
    patient_id = int(input("Enter patient ID to update: "))
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    gender = input("Enter patient gender: ")
    contact = input("Enter patient contact number: ")
    cursor = mydb.cursor()
    sql = "UPDATE Patients SET name = %s, age = %s, gender = %s, contact = %s WHERE Id = %s"
    val = (name, age, gender, contact, patient_id)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) updated.")

# Define the function to delete patient details
def delete_patient():
    patient_id = int(input("Enter patient ID to delete: "))
    cursor = mydb.cursor()
    sql = "DELETE FROM Patients WHERE Id = %s"
    val = (patient_id,)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) deleted.")

# Define the function to add a new doctor
def add_doctor():
    name = input("Enter doctor name: ")
    specialization = input("Enter doctor specialization: ")
    contact = input("Enter doctor contact number: ")
    cursor = mydb.cursor()
    sql = "INSERT INTO Doctors (name, specialization, contact) VALUES (%s, %s, %s)"
    val = (name, specialization, contact)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) inserted.")

# Define the function to view doctor details
def view_doctors():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Doctors")
    result = cursor.fetchall()
    for row in result:
        print(row)

# Define the function to update doctor details
def update_doctor():
    doctor_id = int(input("Enter doctor ID to update: "))
    name = input("Enter doctor name: ")
    specialization = input("Enter doctor specialization: ")
    contact = input("Enter doctor contact number: ")
    cursor = mydb.cursor()
    sql = "UPDATE Doctors SET name = %s, specialization = %s, contact = %s WHERE Id = %s"
    val = (name, specialization, contact, doctor_id)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) updated.")

# Define the function to delete doctor details
def delete_doctor():
    doctor_id = int(input("Enter doctor ID to delete: "))
    cursor = mydb.cursor()
    sql = "DELETE FROM Doctors WHERE Id = %s"
    val = (doctor_id,)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) deleted.")

# Define the function to add a new appointment
def add_appointment():
    patient_id = int(input("Enter patient ID: "))
    doctor_id = int(input("Enter doctor ID: "))
    date = input("Enter appointment date (YYYY-MM-DD): ")
    time = input("Enter appointment time (HH:MM AM/PM): ")
    cursor = mydb.cursor()
    sql = "INSERT INTO Appointments (patient_id, doctor_id, date, time) VALUES (%s, %s, %s, %s)"
    val = (patient_id, doctor_id, date, time)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) inserted.")

# Define the function to view appointment details
def view_appointments():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Appointments")
    result = cursor.fetchall()
    for row in result:
        print(row)

# Define the function to update appointment details
def update_appointment():
    appointment_id = int(input("Enter appointment ID to update: "))
    patient_id = int(input("Enter patient ID: "))
    doctor_id = int(input("Enter doctor ID: "))
    date = input("Enter appointment date (YYYY-MM-DD): ")
    time = input("Enter appointment time (HH:MM AM/PM): ")
    cursor = mydb.cursor()
    sql = "UPDATE Appointments SET patient_id = %s, doctor_id = %s, date = %s, time = %s WHERE Id = %s"
    val = (patient_id, doctor_id, date, time, appointment_id)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) updated.")

# Define the function to delete appointment details
def delete_appointment():
    appointment_id = int(input("Enter appointment ID to delete: "))
    cursor = mydb.cursor()
    sql = "DELETE FROM Appointments WHERE Id = %s"
    val = (appointment_id,)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) deleted.")

# Get the user's choice
def getchoice():
    while True:
        create_database()
        create_patients_table()
        create_doctors_table()
        create_appointments_table()
        
        print("1. Add Patient                            2. View Patients              3. Update Patient              4. Delete Patient")
        print("5. Add Doctor                             6. View Doctors               7. Update Doctor               8. Delete Doctor")
        print("9. Add Appointment                        10. View Appointments         11. Update Appointment         12. Delete Appointment")
        print("13. Exit")
        opp = input("Enter your choice: ")
        if opp == '1':
            add_patient()
            input("Press ENTER KEY to continue.....")
            print()
        elif opp == '2':
            view_patients()
            input("Press ENTER KEY to continue.....")
            print()
        elif opp == '3':
            update_patient()
            input("Press ENTER KEY to continue.....")
            print()
        elif opp == '4':
            delete_patient()
            input("Press ENTER KEY to continue.....")
            print()
        elif opp == '5':
            add_doctor()
            input("Press ENTER KEY to continue.....")
            print()
        elif opp == '6':
            view_doctors()
            input("Press ENTER KEY to continue.....")
            print()
        elif opp == '7':
            update_doctor()
            input("Press ENTER KEY to continue.....")
            print()
        elif opp == '8':
            delete_doctor()
            input("Press ENTER KEY to continue.....")
            print()
        elif opp == '9':
            add_appointment()
            input("Press ENTER KEY to continue.....")
            print()
        elif opp == '10':
            view_appointments()
            input("Press ENTER KEY to continue.....")
            print()
        elif opp == '11':
            update_appointment()
            input("Press ENTER KEY to continue.....")
            print()
        elif opp == '12':
            delete_appointment()
            input("Press ENTER KEY to continue.....")
            print()
        elif opp == '13':
            print('Exited !')
            break

# Recall Choice function
getchoice()
# Disconnecting from the server
mydb.close()
