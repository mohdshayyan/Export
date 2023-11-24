import mysql.connector

# Connect to MySQL server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root")

# Creating a database
def create_database():
    cursor = mydb.cursor()
    cursor.execute('CREATE DATABASE IF NOT EXISTS Covid')
    cursor.execute('USE Covid')
    mydb.commit()
create_database()

# Create tables if not exists
def create_tables():
    cursor = mydb.cursor()
    
    # Patients table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Patients (
            PatientID INT AUTO_INCREMENT PRIMARY KEY,
            FirstName VARCHAR(255),
            LastName VARCHAR(255),
            Age INT,
            Gender VARCHAR(10),
            Status VARCHAR(20)
        )
    ''')

    # TestingCenters table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS TestingCenters (
            CenterID INT AUTO_INCREMENT PRIMARY KEY,
            CenterName VARCHAR(255),
            Location VARCHAR(255),
            Capacity INT
        )
    ''')

    # TestResults table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS TestResults (
            ResultID INT AUTO_INCREMENT PRIMARY KEY,
            PatientID INT,
            CenterID INT,
            Result VARCHAR(10),
            FOREIGN KEY (PatientID) REFERENCES Patients(PatientID),
            FOREIGN KEY (CenterID) REFERENCES TestingCenters(CenterID)
        )
    ''')

    mydb.commit()

# Function to add a patient
def add_patient():
    first_name = input("Enter patient's first name: ")
    last_name = input("Enter patient's last name: ")
    age = int(input("Enter patient's age: "))
    gender = input("Enter patient's gender: ")
    status = input("Enter patient's status: ")

    cursor = mydb.cursor()
    sql = "INSERT INTO Patients (FirstName, LastName, Age, Gender, Status) VALUES (%s, %s, %s, %s, %s)"
    val = (first_name, last_name, age, gender, status)
    cursor.execute(sql, val)
    mydb.commit()
    print("Patient added successfully.")

# Function to view patients
def view_patients():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Patients")
    result = cursor.fetchall()
    for row in result:
        print(row)

# Function to update patient information
def update_patient():
    patient_id = int(input("Enter patient ID to update: "))
    new_status = input("Enter new status: ")

    cursor = mydb.cursor()
    sql = "UPDATE Patients SET Status = %s WHERE PatientID = %s"
    val = (new_status, patient_id)
    cursor.execute(sql, val)
    mydb.commit()
    print("Patient information updated successfully.")

# Function to delete a patient
def delete_patient():
    patient_id = int(input("Enter patient ID to delete: "))

    cursor = mydb.cursor()
    sql = "DELETE FROM Patients WHERE PatientID = %s"
    val = (patient_id,)
    cursor.execute(sql, val)
    mydb.commit()
    print("Patient deleted successfully.")

# Function to add a testing center
def add_testing_center():
    center_name = input("Enter testing center name: ")
    location = input("Enter testing center location: ")
    capacity = int(input("Enter testing center capacity: "))

    cursor = mydb.cursor()
    sql = "INSERT INTO TestingCenters (CenterName, Location, Capacity) VALUES (%s, %s, %s)"
    val = (center_name, location, capacity)
    cursor.execute(sql, val)
    mydb.commit()
    print("Testing center added successfully.")

# Function to view testing centers
def view_testing_centers():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM TestingCenters")
    result = cursor.fetchall()
    for row in result:
        print(row)

# Function to update testing center information
def update_testing_center():
    center_id = int(input("Enter testing center ID to update: "))
    new_capacity = int(input("Enter new capacity: "))

    cursor = mydb.cursor()
    sql = "UPDATE TestingCenters SET Capacity = %s WHERE CenterID = %s"
    val = (new_capacity, center_id)
    cursor.execute(sql, val)
    mydb.commit()
    print("Testing center information updated successfully.")

# Function to delete a testing center
def delete_testing_center():
    center_id = int(input("Enter testing center ID to delete: "))

    cursor = mydb.cursor()
    sql = "DELETE FROM TestingCenters WHERE CenterID = %s"
    val = (center_id,)
    cursor.execute(sql, val)
    mydb.commit()
    print("Testing center deleted successfully.")

# Function to add a test result
def add_test_result():
    patient_id = int(input("Enter patient ID: "))
    center_id = int(input("Enter testing center ID: "))
    result = input("Enter test result: ")

    cursor = mydb.cursor()
    sql = "INSERT INTO TestResults (PatientID, CenterID, Result) VALUES (%s, %s, %s)"
    val = (patient_id, center_id, result)
    cursor.execute(sql, val)
    mydb.commit()
    print("Test result added successfully.")

# Function to view test results
def view_test_results():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM TestResults")
    result = cursor.fetchall()
    for row in result:
        print(row)

# Function to update test result information
def update_test_result():
    result_id = int(input("Enter test result ID to update: "))
    new_result = input("Enter new test result: ")

    cursor = mydb.cursor()
    sql = "UPDATE TestResults SET Result = %s WHERE ResultID = %s"
    val = (new_result, result_id)
    cursor.execute(sql, val)
    mydb.commit()
    print("Test result information updated successfully.")

# Function to delete a test result
def delete_test_result():
    result_id = int(input("Enter test result ID to delete: "))

    cursor = mydb.cursor()
    sql = "DELETE FROM TestResults WHERE ResultID = %s"
    val = (result_id,)
    cursor.execute(sql, val)
    mydb.commit()
    print("Test result deleted successfully.")

# Main function
def main():
    create_tables()
    while True:
        print("\n--- Covid-19 Analysis ---")
        print("1. Patients\n2. Testing Centers\n3. Test Results\n4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            patients_menu()
        elif choice == 2:
            testing_centers_menu()
        elif choice == 3:
            test_results_menu()
        elif choice == 4:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Menu for Patients
def patients_menu():
    while True:
        print("\n--- Patients Menu ---")
        print("1. Add Patient\n2. View Patients\n3. Update Patient\n4. Delete Patient\n5. Back")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_patient()
        elif choice == 2:
            view_patients()
        elif choice == 3:
            update_patient()
        elif choice == 4:
            delete_patient()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

# Menu for Testing Centers
def testing_centers_menu():
    while True:
        print("\n--- Testing Centers Menu ---")
        print("1. Add Testing Center\n2. View Testing Centers\n3. Update Testing Center\n4. Delete Testing Center\n5. Back")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_testing_center()
        elif choice == 2:
            view_testing_centers()
        elif choice == 3:
            update_testing_center()
        elif choice == 4:
            delete_testing_center()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

# Menu for Test Results
def test_results_menu():
    while True:
        print("\n--- Test Results Menu ---")
        print("1. Add Test Result\n2. View Test Results\n3. Update Test Result\n4. Delete Test Result\n5. Back")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_test_result()
        elif choice == 2:
            view_test_results()
        elif choice == 3:
            update_test_result()
        elif choice == 4:
            delete_test_result()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()

# Disconnect from the MySQL server
mydb.close()
