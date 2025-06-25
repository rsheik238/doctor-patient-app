import sqlite3
from typing import List
from app.domain.models import Doctor, Patient, Visit
from app.domain.repositories import DoctorRepository, PatientRepository, VisitRepository

class SQLiteDoctorRepository(DoctorRepository):
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def add(self, first_name: str, last_name: str, qualification: str, specialization: str,
            work_location: str, address: str, phone_number: str) -> Doctor:
        cur = self.conn.cursor()
        cur.execute("""
            INSERT INTO doctors (first_name, last_name, qualification, specialization,
                                 work_location, address, phone_number)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (first_name, last_name, qualification, specialization,
              work_location, address, phone_number))
        self.conn.commit()
        return Doctor(id=cur.lastrowid, first_name=first_name, last_name=last_name,
                      qualification=qualification, specialization=specialization,
                      work_location=work_location, address=address, phone_number=phone_number)

    def get_all(self) -> List[Doctor]:
        cur = self.conn.cursor()
        cur.execute("SELECT id, first_name, last_name, qualification, specialization, work_location, address, phone_number FROM doctors")
        return [
            Doctor(*row) for row in cur.fetchall()
        ]

    def get_work_locations(self) -> List[str]:
        cur = self.conn.cursor()
        cur.execute("SELECT DISTINCT work_location FROM doctors")
        return [row[0] for row in cur.fetchall()]


class SQLitePatientRepository(PatientRepository):
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def add(self, first_name: str, last_name: str, address: str, phone_number: str,
            date_of_birth: str, sex: str, nearest_hospital_location: str) -> Patient:
        # Validate nearest_hospital_location exists in doctors table
        cur = self.conn.cursor()
        cur.execute("SELECT COUNT(*) FROM doctors WHERE work_location = ?", (nearest_hospital_location,))
        count = cur.fetchone()[0]
        if count == 0:
            raise ValueError("Invalid nearest_hospital_location: no doctor works at this location.")

        cur.execute("""
            INSERT INTO patients (first_name, last_name, address, phone_number,
                                  date_of_birth, sex, nearest_hospital_location)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (first_name, last_name, address, phone_number, date_of_birth, sex, nearest_hospital_location))
        self.conn.commit()
        return Patient(id=cur.lastrowid, first_name=first_name, last_name=last_name,
                       address=address, phone_number=phone_number,
                       date_of_birth=date_of_birth, sex=sex, nearest_hospital_location=nearest_hospital_location)

    def get_all(self) -> List[Patient]:
        cur = self.conn.cursor()
        cur.execute("SELECT id, first_name, last_name, address, phone_number, date_of_birth, sex, nearest_hospital_location FROM patients")
        return [
            Patient(*row) for row in cur.fetchall()
        ]

class SQLiteVisitRepository(VisitRepository):
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def add(self, doctor_id: int, patient_id: int, date: str, time: str) -> Visit:
        cur = self.conn.cursor()
        cur.execute("""
            INSERT INTO visits (doctor_id, patient_id, date, time)
            VALUES (?, ?, ?, ?)
        """, (doctor_id, patient_id, date, time))
        self.conn.commit()
        return Visit(id=cur.lastrowid, doctor_id=doctor_id, patient_id=patient_id, date=date, time=time)

    def get_all(self) -> List[Visit]:
        cur = self.conn.cursor()
        cur.execute("SELECT id, doctor_id, patient_id, date, time FROM visits")
        return [Visit(*row) for row in cur.fetchall()]
