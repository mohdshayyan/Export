import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

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

# Function to generate and display various graphs
def generate_graphs():
    print("PRESS=>(1-6)")
    choice = int(input("Enter your choice: "))
    if choice == 1:# Histogram of Patient Ages
        cursor = mydb.cursor()
        cursor.execute("SELECT Age FROM Patients")
        ages = cursor.fetchall()
        ages = [age[0] for age in ages]
        plt.hist(ages, bins=20, color='blue', edgecolor='black')
        plt.title('Histogram of Patient Ages')
        plt.xlabel('Age')
        plt.ylabel('Frequency')
        plt.show()
    elif choice == 2: # Pie chart of Gender distribution
        cursor = mydb.cursor()        
        cursor.execute("SELECT Gender, COUNT(*) FROM Patients GROUP BY Gender")
        gender_counts = cursor.fetchall()
        genders = [gender[0] for gender in gender_counts]
        counts = [count[1] for count in gender_counts]
        plt.pie(counts, labels=genders, autopct='%1.1f%%', startangle=140)
        plt.title('Gender Distribution of Patients')
        plt.show()
    elif choice == 3:
        cursor = mydb.cursor()        
    # Bar chart of Testing Center Capacities
        cursor.execute("SELECT CenterName, Capacity FROM TestingCenters")
        center_data = cursor.fetchall()
        centers = [center[0] for center in center_data]
        capacities = [capacity[1] for capacity in center_data]
        plt.bar(centers, capacities, color='green')
        plt.xlabel('Testing Center')
        plt.ylabel('Capacity')
        plt.title('Testing Center Capacities')
        plt.xticks(rotation=45, ha="right")
        plt.show()
    elif choice == 4:
    # Line chart of Patient Status changes
        cursor = mydb.cursor()    
        cursor.execute("SELECT PatientID, Status FROM Patients")
        status_data = cursor.fetchall()
        patients = [patient[0] for patient in status_data]
        statuses = [status[1] for status in status_data]
        plt.plot(patients, statuses, marker='o')
        plt.xlabel('Patient ID')
        plt.ylabel('Status')
        plt.title('Patient Status Changes')
        plt.show()
    elif choice == 5:
    # Scatter plot of Patient Ages and Testing Center Capacities
        cursor = mydb.cursor()
        cursor.execute("SELECT Age FROM Patients")
        patient_ages = cursor.fetchall()
        patient_ages = [age[0] for age in patient_ages]
        cursor.execute("SELECT Capacity FROM TestingCenters")
        center_capacities = cursor.fetchall()
        center_capacities = [capacity[0] for capacity in center_capacities]
        plt.scatter(patient_ages, center_capacities, color='red')
        plt.xlabel('Patient Age')
        plt.ylabel('Testing Center Capacity')
        plt.title('Scatter Plot of Patient Ages and Testing Center Capacities')
        plt.show()
    elif choice == 6:
# Box plot of Patient Ages
        cursor = mydb.cursor()    
        cursor.execute("SELECT Age FROM Patients")
        patient_ages_data = cursor.fetchall()
        patient_ages = [age[0] for age in patient_ages_data]
        plt.boxplot([patient_ages])
        plt.title('Box Plot of Patient Ages')
        plt.xlabel('Patients')
        plt.ylabel('Age')
        plt.show()



# Main function
def main():
    create_tables()
    while True:
        print("\n--- Covid-19 Analysis ---")
        print("1. Patient Module\n2. Testing Centers Module\n3. Test Results Module\n4. Generate Graphs Module\n5. Exit Module")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            patients_menu()
        elif choice == 2:
            testing_centers_menu()
        elif choice == 3:
            test_results_menu()
        elif choice == 4:
            print("1.Graph\n2.Graph \n3.Graph \n4.Graph \n5.Graph \n6.Graph ")
            generate_graphs()
        elif choice == 5:
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
