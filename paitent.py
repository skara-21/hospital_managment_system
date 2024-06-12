from typing import List
from appointment import Appointment

class Patient:
    def __init__(self,name:str,age:int,gender:str,patient_id:int) -> None:
        self.name=name
        self.age=age
        self.gender=gender
        self.patient_id=patient_id
        self.history: List[str] = []
        self.appointments: List[Appointment]=[]
    
    def get_details(self) -> str:
        if len(self.history) !=0:
            history=f"History: {str(self.history)}"
        else: 
            history=""
        return (f"Patient ID: {self.patient_id}\n"
                f"Name: {self.name}\n"
                f"Age: {self.age}\n"
                f"Gender: {self.gender}\n"
                f"{history}\n")
    
    def add_history(self,entry:str):
        self.history.append(entry)
        
    def add_appointment(self,appointment:Appointment):
        self.appointments.append(appointment)
        
    def get_upcoming_appointment(self):
        self.appointments.sort(key=lambda appointment: appointment.datetime)
        return self.appointments[0] if self.appointments else None
        
        
    
        