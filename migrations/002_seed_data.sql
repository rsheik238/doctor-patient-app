-- Insert 5 doctors
INSERT INTO doctors (first_name, last_name, qualification, specialization, work_location, address, phone_number)
VALUES
('Aisha', 'Khan', 'MBBS, MD', 'Cardiology', 'Greenwood Hospital', '123 Heart Ave', '9876543210'),
('Raj', 'Patel', 'MBBS, MS', 'Orthopedics', 'Sunrise Medical Center', '456 Bone St', '9123456780'),
('Sara', 'Lee', 'MBBS', 'Dermatology', 'Maple Clinic', '789 Skin Rd', '9345678901'),
('Daniel', 'Smith', 'MBBS, DM', 'Neurology', 'NeuroCare Hospital', '321 Brain Ln', '9988776655'),
('Fatima', 'Ahmed', 'MBBS, DGO', 'Gynecology', 'Sunrise Medical Center', '654 Women St', '9871234567');

-- Insert 15 patients (3 per hospital location)
INSERT INTO patients (first_name, last_name, address, phone_number, date_of_birth, sex, nearest_hospital_location)
VALUES
('John', 'Doe', '101 Main St', '8881110001', '1990-01-01', 'M', 'Greenwood Hospital'),
('Emily', 'Brown', '102 Main St', '8881110002', '1985-05-10', 'F', 'Greenwood Hospital'),
('Carlos', 'Vega', '103 Main St', '8881110003', '2000-07-21', 'M', 'Greenwood Hospital'),

('Priya', 'Nair', '201 Oak St', '8881110004', '1992-08-14', 'F', 'Sunrise Medical Center'),
('Abdul', 'Rahman', '202 Oak St', '8881110005', '1988-03-03', 'M', 'Sunrise Medical Center'),
('Maya', 'Reddy', '203 Oak St', '8881110006', '1975-11-25', 'F', 'Sunrise Medical Center'),

('Tom', 'Watson', '301 Elm St', '8881110007', '1999-12-12', 'M', 'Maple Clinic'),
('Sofia', 'Chen', '302 Elm St', '8881110008', '1996-04-18', 'F', 'Maple Clinic'),
('Rehan', 'Ali', '303 Elm St', '8881110009', '1980-10-05', 'M', 'Maple Clinic'),

('Linda', 'Gomez', '401 Birch St', '8881110010', '1994-09-30', 'F', 'NeuroCare Hospital'),
('David', 'Kim', '402 Birch St', '8881110011', '1993-06-20', 'M', 'NeuroCare Hospital'),
('Rina', 'Das', '403 Birch St', '8881110012', '1981-08-08', 'F', 'NeuroCare Hospital'),

('Aliya', 'Hassan', '501 Pine St', '8881110013', '2002-02-22', 'F', 'Sunrise Medical Center'),
('Mohammed', 'Iqbal', '502 Pine St', '8881110014', '1997-03-17', 'M', 'Sunrise Medical Center'),
('Julia', 'White', '503 Pine St', '8881110015', '1989-12-03', 'F', 'Sunrise Medical Center');
