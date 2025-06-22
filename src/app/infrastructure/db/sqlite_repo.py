import sqlite3
from typing import List
from app.domain.models import Doctor, Patient, Visit
from app.domain.repositories import DoctorRepository, PatientRepository, VisitRepository

class SQLiteDoctorRepository(DoctorRepository):
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
    def add(self, name: str) -> Doctor:
        cur = self.conn.cursor()
        cur.execute("INSERT INTO doctors (name) VALUES (?)", (name,))
        self.conn.commit()
        return Doctor(id=cur.lastrowid, name=name)
    def get_all(self) -> List[Doctor]:
        cur = self.conn.cursor()
        cur.execute("SELECT id, name FROM doctors")
        return [Doctor(id=row[0], name=row[1]) for row in cur.fetchall()]

class SQLitePatientRepository(PatientRepository):
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
    def add(self, name: str) -> Patient:
        cur = self.conn.cursor()
        cur.execute("INSERT INTO patients (name) VALUES (?)", (name,))
        self.conn.commit()
        return Patient(id=cur.lastrowid, name=name)
    def get_all(self) -> List[Patient]:
        cur = self.conn.cursor()
        cur.execute("SELECT id, name FROM patients")
        return [Patient(id=row[0], name=row[1]) for row in cur.fetchall()]

class SQLiteVisitRepository(VisitRepository):
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
    def add(self, doctor_name: str, patient_name: str, date: str, time: str) -> Visit:
        cur = self.conn.cursor()
        cur.execute("""
            INSERT INTO visits (doctor_id, patient_id, date, time)
            VALUES ((SELECT id FROM doctors WHERE name=?), (SELECT id FROM patients WHERE name=?), ?, ?)
        """, (doctor_name, patient_name, date, time))
        self.conn.commit()
        return Visit(id=cur.lastrowid, doctor_id=0, patient_id=0, date=date, time=time)
    def get_all(self) -> List[Visit]:
        cur = self.conn.cursor()
        cur.execute("SELECT id, doctor_id, patient_id, date, time FROM visits")
        return [Visit(*row) for row in cur.fetchall()]
