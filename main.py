from paitent import Patient
from medical_staff import Medical_Staff
from appointment import Appointment
from hospital_manager import Hospital_Manager

def print_menu():
    print("\nHospital Management System")
    print("1. Add Patient")
    print("2. Add Medical Staff")
    print("3. Add Appointment")
    print("4. Get Patient Information")
    print("5. Update Patient History")
    print("6. View Upcoming Appointments For Patient")
    print("7. View Upcoming Appointments For Doctor")
    print("0. Exit")

def add_patient(hospital_manager):
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    gender = input("Enter patient gender: ")
    patient_id = int(input("Enter patient ID: "))
    patient = Patient(name, age, gender, patient_id)
    hospital_manager.add_patient(patient)
    print("Patient added successfully.")

def add_medical_staff(hospital_manager):
    staff_id = int(input("Enter staff ID: "))
    name = input("Enter staff name: ")
    position = input("Enter staff position: ")
    staff = Medical_Staff(staff_id, name, position)
    hospital_manager.add_med_staff(staff)
    print("Medical staff added successfully.")

def add_appointment(hospital_manager,appointment_id):
    patient_id = (input("Enter patient ID: "))
    staff_id = (input("Enter doctor ID: "))
    if patient_id.isdigit() and staff_id.isdigit():
        patient_id=int(patient_id)
        staff_id=int(staff_id)
        if hospital_manager.valid_patient(patient_id) and hospital_manager.valid_doc(staff_id):
            date = input("Enter date (YYYY-MM-DD): ")
            time = input("Enter time (HH:MM): ")
            appointment = Appointment(appointment_id, patient_id, staff_id, date, time)
            hospital_manager.add_appointment(appointment)
            print("Appointment added successfully.")
        else:
            print("Invalid Doctor/Paitent information")
    else:
        print("Invalid Doctor/Paitent ID")
        

def get_patient_information(hospital_manager):
    patient_id = (input("Enter patient's ID: "))
    if patient_id.isdigit():
        patient_id=int(patient_id)
        if hospital_manager.valid_patient(patient_id):
            hospital_manager.get_patient_info(patient_id)
        else:
            print("This paitent is not in out database")
    else:
        print("Please enter a valid patient ID")

def update_patient_history(hospital_manager):
    patient_id = (input("Enter patient's ID: "))
    staff_id = (input("Enter staff's ID: "))
    if patient_id.isdigit() and staff_id.isdigit():
        patient_id=int(patient_id)
        staff_id=int(staff_id)
        appointment=hospital_manager.get_upcoming_appointment_patient(patient_id)
        if hospital_manager.valid_patient(patient_id) and hospital_manager.valid_doc(staff_id):
            history = input("Enter patient's history update: ")
            hospital_manager.update_patient_history(patient_id, staff_id, history,appointment)
        else:
            print("Invalid Doctor/Paitent information")
    else:
        print("Invalid Doctor/Paitent ID")
        
def view_upcoming_appointments_patient(hospital_manager):
    patient_id = input("Enter patient's ID: ")
    if patient_id.isdigit():
        patient_id=int(patient_id)
        if hospital_manager.get_upcoming_appointment_patient(patient_id) is not None:
            print("\nUpcoming Appointments:")
            print(hospital_manager.get_upcoming_appointment_patient(patient_id).get_details())
        else:
            print("This patient has no upcoming appointments")
    else:
        print("Please enter a valid patient ID")    
        
def view_upcoming_appointments_doctor(hospital_manager):
    doctor_id=input("Enter doctor's ID: ")
    if doctor_id.isdigit():
        doctor_id=int(doctor_id)
        if hospital_manager.get_upcoming_appointment_doctor(doctor_id) is not None:
            print("\nUpcoming Appointments:")
            print(hospital_manager.get_upcoming_appointment_doctor(doctor_id).get_details())
        else:
            print("This doctor has no upcoming appointments")
    else:
        print("Please enter a valid doctor ID")    

def main():
    hospital_manager = Hospital_Manager()
    hospital_manager.load_data()
    appointment_id=len(hospital_manager.appointments)+1
    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_patient(hospital_manager)
        elif choice == '2':
            add_medical_staff(hospital_manager)
        elif choice == '3':
            add_appointment(hospital_manager,appointment_id)
            appointment_id+=1
        elif choice == '4':
            get_patient_information(hospital_manager)
        elif choice == '5':
            update_patient_history(hospital_manager)
        elif choice == '6':
            view_upcoming_appointments_patient(hospital_manager)
        elif choice=='7':
            view_upcoming_appointments_doctor(hospital_manager)
        elif choice == '0':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()