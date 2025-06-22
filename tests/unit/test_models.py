from app.domain.models import Doctor, Patient, Visit

def test_doctor_model():
    doc = Doctor(id=1, name="Dr. Smith")
    assert doc.name == "Dr. Smith"

def test_patient_model():
    pat = Patient(id=1, name="Alice")
    assert pat.name == "Alice"

def test_visit_model():
    visit = Visit(id=1, doctor_id=1, patient_id=1, date="2024-01-01", time="10:00")
    assert visit.date == "2024-01-01"
