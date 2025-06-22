import sqlite3
from app.infrastructure.db.sqlite_repo import (
    SQLiteDoctorRepository,
    SQLitePatientRepository,
    SQLiteVisitRepository
)

class Container:
    def __init__(self, db_path="hospital.db"):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self._setup_db()

        self.doctor_repo = SQLiteDoctorRepository(self.conn)
        self.patient_repo = SQLitePatientRepository(self.conn)
        self.visit_repo = SQLiteVisitRepository(self.conn)

    def _setup_db(self):
        cur = self.conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS doctors(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL)""")
        cur.execute("""CREATE TABLE IF NOT EXISTS patients(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL)""")
        cur.execute("""CREATE TABLE IF NOT EXISTS visits(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            doctor_id INTEGER,
            patient_id INTEGER,
            date TEXT,
            time TEXT,
            FOREIGN KEY (doctor_id) REFERENCES doctors(id),
            FOREIGN KEY (patient_id) REFERENCES patients(id))""")
        self.conn.commit()
