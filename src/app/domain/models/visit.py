from dataclasses import dataclass

@dataclass
class Visit:
    id: int
    doctor_id: int
    patient_id: int
    date: str
    time: str
