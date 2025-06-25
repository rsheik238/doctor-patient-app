from dataclasses import dataclass

@dataclass
class Doctor:
    id: int
    first_name: str
    last_name: str
    qualification: str
    specialization: str
    work_location: str
    address: str
    phone_number: str