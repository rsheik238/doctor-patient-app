-- DROP OLD TABLES IF THEY EXIST
DROP TABLE IF EXISTS doctors;
DROP TABLE IF EXISTS patients;

-- CREATE UPDATED DOCTORS TABLE
CREATE TABLE doctors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    qualification TEXT,
    specialization TEXT,
    work_location TEXT NOT NULL,
    address TEXT,
    phone_number TEXT
);

-- CREATE UPDATED PATIENTS TABLE
CREATE TABLE patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    address TEXT,
    phone_number TEXT,
    date_of_birth TEXT,
    sex TEXT,
    nearest_hospital_location TEXT NOT NULL
);

-- OPTIONAL: ENSURE patients.nearest_hospital_location MATCHES doctors.work_location
-- This is enforced in code logic, not via foreign key
