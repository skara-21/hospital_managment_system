from typing import List
from appointment import Appointment

class Medical_Staff:
    def __init__(self,staff_id:int,name:str,position:str) -> None:
        self.staff_id=staff_id
        self.name=name
        self.position=position
        self.schedule: List[Appointment]=[]
        
    def add_appointment(self,appointment:Appointment):
        self.schedule.append(appointment)
        
    def get_upcoming_appointment(self):
        self.schedule.sort(key=lambda appointment: appointment.datetime)
        return self.schedule[0] if self.schedule else None