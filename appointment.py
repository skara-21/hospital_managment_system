from datetime import datetime
class Appointment:
    def __init__(self,appointment_id:int,patient_id:int,doctor_id:int,date:str,time:str) -> None:
        self.appointment_id=appointment_id
        self.patient_id=patient_id
        self.doctor_id=doctor_id
        self.datetime = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
        
    def get_details(self):
        return (f"Appointment_id: {self.appointment_id}\n"
                f"Patient ID: {self.patient_id}\n"
                f"Doctor ID: {self.doctor_id}\n"
                f"Appointment Date: {self.datetime.strftime("%Y-%m-%d %H:%M")}\n")