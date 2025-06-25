from dataclasses import dataclass

@dataclass
class Patient:
    id: int
    first_name: str
    last_name: str
    address: str
    phone_number: str
    date_of_birth: str  # store as YYYY-MM-DD
    sex: str            # e.g. "M", "F", "Other"
    nearest_hospital_location: str  # must match a doctor's work_location
