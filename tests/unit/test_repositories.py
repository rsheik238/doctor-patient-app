import sqlite3
from app.infrastructure.db.sqlite_repo import (
    SQLiteDoctorRepository, SQLitePatientRepository, SQLiteVisitRepository
)

def test_doctor_repo_add_and_get():
    conn = sqlite3.connect(":memory:")
    repo = SQLiteDoctorRepository(conn)
    conn.execute("CREATE TABLE doctors (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL)")
    doc = repo.add("Dr. A")
    assert doc.name == "Dr. A"
    assert len(repo.get_all()) == 1

def test_patient_repo_add_and_get():
    conn = sqlite3.connect(":memory:")
    repo = SQLitePatientRepository(conn)
    conn.execute("CREATE TABLE patients (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL)")
    pat = repo.add("John")
    assert pat.name == "John"
    assert len(repo.get_all()) == 1

def test_visit_repo_add_and_get():
    conn = sqlite3.connect(":memory:")
    conn.executescript("""
    CREATE TABLE doctors (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL);
    CREATE TABLE patients (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL);
    CREATE TABLE visits (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        doctor_id INTEGER,
        patient_id INTEGER,
        date TEXT,
        time TEXT
    );
    INSERT INTO doctors (name) VALUES ('Dr. A');
    INSERT INTO patients (name) VALUES ('John');
    """)
    repo = SQLiteVisitRepository(conn)
    visit = repo.add("Dr. A", "John", "2024-01-01", "10:00")
    assert visit.date == "2024-01-01"
    assert len(repo.get_all()) == 1
