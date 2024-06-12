from typing import List
from medical_staff import Medical_Staff
from paitent import Patient
from appointment import Appointment
import os

class Hospital_Manager:
    def __init__(self) -> None:
        self.patients: List[Patient] = []
        self.appointments: List[Appointment] = []
        self.staff: List[Medical_Staff] = []
        
    def add_patient(self,patient:Patient):
        self.patients.append(patient)
        pat_file_path=os.path.join(os.getcwd(),'patient_files')
        if os.path.isdir(pat_file_path):
            file_path=os.path.join(pat_file_path,f"{patient.patient_id}.txt")
            with open(file_path,'w') as f:
                f.write(patient.get_details())
            
        
    def add_appointment(self,appointment:Appointment):
        self.appointments.append(appointment)
        appointment_files_path=os.path.join(os.getcwd(),'appointments')
        if os.path.isdir(appointment_files_path):
            file_path=os.path.join(appointment_files_path,f"{appointment.appointment_id}.txt")
            with open(file_path,'w') as f:
                f.write(appointment.get_details())
        self.add_appointment_to_schedules(appointment.patient_id,appointment.doctor_id,appointment)
        
    def add_appointment_to_schedules(self,patient_id,doctor_id,appointment):
        for patient in self.patients:
                if patient.patient_id==patient_id: 
                    patient.appointments.append(appointment)
                    break
        for staff in self.staff:
            if staff.staff_id==doctor_id:
                staff.schedule.append(appointment)
                break  
            
    def valid_patient(self, paitent_id):
        for p in self.patients:
            if p.patient_id==paitent_id:
                return True
        return False
    
    def valid_doc(self,doctor_id):
        for d in self.staff:
            if d.staff_id==doctor_id:
                return True
        return False
        
    def add_med_staff(self,med_staff:Medical_Staff):
        self.staff.append(med_staff)
        med_file_path=os.path.join(os.getcwd(),'medical_staff_files',f"{med_staff.staff_id}.txt")
        with open(med_file_path,'w') as f:
            f.write(f"Name: {med_staff.name}\n")
            f.write(f"Position: {med_staff.position}\n")
            f.write("History \n")
        
    def file_to_str(self,file,pat_file_path) ->None :
        try:
            file_path=os.path.join(pat_file_path,file)
            with open(file_path, 'r') as file:
                file_content = file.read()
                print(file_content)
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
        
    def get_patient_info(self,patient_id:int):
        pat_file_path=os.path.join(os.getcwd(),'patient_files')
        pat_file_name=f"{patient_id}.txt"
        if os.path.isdir(pat_file_path):
            os.chdir(pat_file_path)
            contents=os.listdir(pat_file_path)
            for file in contents:
                if file==pat_file_name:
                    self.file_to_str(file,pat_file_path)
                    return
        print("Such file is not in our database")     
        
    def update_file(self,file,path,staff_id,history,appointment:Appointment):
        pathp=os.path.join(path,'patient_files')
        if os.path.isdir(pathp):
            os.chdir(pathp)
            with open(os.path.join(pathp,file),'a') as f:
                f.write("During the appointment: \n")
                f.write(appointment.get_details())
                f.write("Following conclusions were reached: \n")
                f.write(history)
                f.write("\n")
        pathm=os.path.join(path,'medical_staff_files')
        if os.path.isdir(pathm):
            os.chdir(pathm)
            with open(os.path.join(pathm,f"{staff_id}.txt"),'a')as f:
                f.write("\n")
                f.write("During the appointment: \n")
                f.write(appointment.get_details())
                f.write("Following conclusions were reached: \n")
                f.write(history)
                f.write("\n")
                
    def remove_appointment_from_schedules(self,patient_id,staff_id,appointment):
        for patient in self.patients:
            if patient.patient_id==patient_id:
                patient.appointments.remove(appointment)
                break
        for staff in self.staff:
            if staff.staff_id==staff_id:
                staff.schedule.remove(appointment)
                return
        
    def update_patient_history(self,patient_id:int,staff_id:int,history,appointment:Appointment):
        path=os.getcwd()
        pat_file_path=os.path.join(path,'patient_files')
        pat_file_name=f"{patient_id}.txt"
        if os.path.isdir(pat_file_path):
            os.chdir(pat_file_path)
            contents=os.listdir(pat_file_path)
            for file in contents:
                if file==pat_file_name:
                    self.update_file(file,path,staff_id,history,appointment)
                    self.remove_appointment_from_schedules(patient_id,staff_id,appointment)
                    return
            else:
                print("Patient's file not found")      
    
    def create_patient_history(self,patient:Patient,special_info:str):
        self.patients.append(patient)
        pat_file_path=os.path.join(os.getcwd(),'patient_files',f"{patient.patient_id}.txt")
        with open(pat_file_path,'w') as f:
            f.write(f"Name: {patient.name}\n")
            f.write(f"Age: {patient.age}\n")
            f.write(f"Gender: {patient.gender}\n")
            if special_info:
                f.write(f"Special info: {special_info}\n")
            f.write("History: \n")
    
    def get_upcoming_appointment_patient(self,patient_id:int):
        for patient in self.patients:
            if patient.patient_id==patient_id:
                appointment=patient.get_upcoming_appointment()
                if appointment is not None:
                    return appointment
                else:
                    print("This patient doesn't have any upcoming appointments")
        else:
            print("This patient doesn't exist")
        return None
            
    def get_upcoming_appointment_doctor(self,staff_id:int):
        for staff in self.staff:
            if staff.staff_id==staff_id:
                appointment=staff.get_upcoming_appointment()
                if appointment is not None:
                    return appointment
                else:
                    print("This staff member doesn't have any upcoming appointments")
        else:
            print("This staff member doesn't exist") 
        return None
                 
    def load_data(self):
        patient_files_path = os.path.join(os.getcwd(), 'patient_files')
        if os.path.isdir(patient_files_path):
            for file_name in os.listdir(patient_files_path):
                file_path = os.path.join(patient_files_path, file_name)
                if os.path.isfile(file_path) and file_path.endswith('.txt'):
                    patient_id=file_name[:-4]
                    with open(file_path, 'r') as file:
                        patient_data = self.parse_patient_file(file.read())
                        patient = Patient(patient_data['Name'],patient_data['Age'],patient_data['Gender'],int(patient_id))
                        self.patients.append(patient)
        
        staff_files_path = os.path.join(os.getcwd(), 'medical_staff_files')
        if os.path.isdir(staff_files_path):
            for file_name in os.listdir(staff_files_path):
                file_path = os.path.join(staff_files_path, file_name)
                if os.path.isfile(file_path) and file_path.endswith('.txt'):
                    staff_id=file_name[:-4]
                    with open(file_path, 'r') as file:
                        staff_data = self.parse_staff_file(file.read())
                        staff_member = Medical_Staff(int(staff_id),staff_data['Name'],staff_data['Position'])
                        self.staff.append(staff_member)
                        
        appointment_files_path=os.path.join(os.getcwd(),'appointments')
        if os.path.isdir(appointment_files_path):
            for file_name in os.listdir(appointment_files_path):
                file_path = os.path.join(appointment_files_path, file_name)
                if os.path.isfile(file_path) and file_path.endswith('.txt'):
                    with open(file_path, 'r') as file:
                        app_data=self.parse_appointment_file(file.read())
                        appointment=Appointment(app_data['Appointment_id'],int(app_data['Patient ID']),int(app_data['Doctor ID']),app_data['Date'],app_data['Time'])
                        self.appointments.append(appointment)
                        
        self.fill_in_appointments()
                        
    def fill_in_appointments(self):
        for appointment in self.appointments:
            patient_id=appointment.patient_id
            doctor_id=appointment.doctor_id
            self.add_appointment_to_schedules(patient_id,doctor_id,appointment)
                        
    def parse_appointment_file(self,file_content:str):
        appointment_map = {}
        for line in file_content.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                appointment_map[key.strip()] = value.strip()
        if 'Appointment Date' in appointment_map:
            date_str, time_str = appointment_map['Appointment Date'].split(' ', 1)
            appointment_map['Date'] = date_str.strip()
            appointment_map['Time'] = time_str.strip()
        return appointment_map

                           
    def parse_patient_file(self, file_content: str):
        patient_data = {}
        for line in file_content.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                patient_data[key.strip()] = value.strip()
            
        return patient_data
    
    def parse_staff_file(self, file_content: str):
        staff_data = {}
        for line in file_content.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                staff_data[key.strip()] = value.strip()
        return staff_data
