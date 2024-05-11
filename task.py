import os

class Patient:
    def __init__(self, name, age, gender, condition, status="In Treatment"):
        self.name = name
        self.age = age
        self.gender = gender
        self.condition = condition
        self.status = status

    def update_status(self, new_status):
        self.status = new_status

class ClinicManagementSystem:
    def __init__(self, file_name):
        self.file_name = file_name
        if not os.path.exists(self.file_name):
            open(self.file_name, 'w').close()  # Create the file if it doesn't exist
        self.all_patients = []

    def load_patients(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as file:
                for line in file:
                    patient_data = line.strip().split(',')
                    patient = Patient(*patient_data)
                    self.all_patients.append(patient)
            print("Patients loaded successfully.")
        else:
            print("Patient file does not exist.")

    def save_patients(self):
        with open(self.file_name, 'w') as file:
            for patient in self.all_patients:
                file.write(f"{patient.name},{patient.age},{patient.gender},{patient.condition},{patient.status}\n")
        print("Patients saved successfully.")

    def add_patient(self, name, age, gender, condition):
        patient = Patient(name, age, gender, condition)
        self.all_patients.append(patient)
        self.save_patients()
        print("Patient added successfully.")

    def view_patients(self):
        if not self.all_patients:
            print("No patients in the system.")
        else:
            for idx, patient in enumerate(self.all_patients, start=1):
                print(f"Patient {idx}:")
                print(f"Name: {patient.name}")
                print(f"Age: {patient.age}")
                print(f"Gender: {patient.gender}")
                print(f"Condition: {patient.condition}")
                print(f"Status: {patient.status}")
                print()

    def update_patient_status(self, idx, new_status):
        if 1 <= idx <= len(self.all_patients):
            self.all_patients[idx - 1].update_status(new_status)
            self.save_patients()
            print("Patient status updated successfully.")
        else:
            print("Invalid patient index.")

    def remove_patient(self, idx):
        if 1 <= idx <= len(self.all_patients):
            del self.all_patients[idx - 1]
            self.save_patients()
            print("Patient removed successfully.")
        else:
            print("Invalid patient index.")

def validate_input(name, age, gender, condition):
    if not name or not age or not gender or not condition:
        return False
    try:
        int(age)
    except ValueError:
        return False
    return True

def main():
    file_name = "patients.txt"
    clinic = ClinicManagementSystem(file_name)
    clinic.load_patients()
    
    while True:
        print("Clinic Management System Menu:")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Mark Patient as Completed")
        print("4. Remove Patient")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter patient name: ")
            age = input("Enter patient age: ")
            gender = input("Enter patient gender: ")
            condition = input("Enter patient condition: ")
            if validate_input(name, age, gender, condition):
                clinic.add_patient(name, age, gender, condition)
            else:
                print("Invalid input. Please try again.")
        
        elif choice == '2':
            clinic.view_patients()
        
        elif choice == '3':
            idx = int(input("Enter the index of the patient to mark as completed: "))
            new_status = input("Enter the new status (e.g. Treated, Completed): ")
            clinic.update_patient_status(idx, new_status)
        
        elif choice == '4':
            idx = int(input("Enter the index of the patient to remove: "))
            clinic.remove_patient(idx)
        
        elif choice == '5':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
