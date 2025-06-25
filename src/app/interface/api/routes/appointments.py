from flask import Blueprint, request, jsonify
import sqlite3
from app.infrastructure.db.sqlite_repo import SQLiteVisitRepository

appointments_bp = Blueprint("appointments", __name__, url_prefix="/appointments")

@appointments_bp.route("", methods=["GET"])
def get_appointments():
    conn = sqlite3.connect("hospital.db")
    repo = SQLiteVisitRepository(conn)

    doctor_id = request.args.get("doctor_id", type=int)
    patient_id = request.args.get("patient_id", type=int)
    date = request.args.get("date")

    visits = repo.get_all()

    filtered = [
        visit for visit in visits
        if (not doctor_id or visit.doctor_id == doctor_id)
        and (not patient_id or visit.patient_id == patient_id)
        and (not date or visit.date == date)
    ]

    return jsonify([
        {
            "id": visit.id,
            "doctor_id": visit.doctor_id,
            "patient_id": visit.patient_id,
            "date": visit.date,
            "time": visit.time
        }
        for visit in filtered
    ])
