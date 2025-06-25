from flask import Blueprint, request, jsonify
import sqlite3
from datetime import datetime, timedelta

slots_bp = Blueprint("slots", __name__, url_prefix="/slots")

def generate_all_slots():
    morning = [datetime.strptime("09:00", "%H:%M") + timedelta(minutes=30*i) for i in range(6)]   # 9 to 12
    afternoon = [datetime.strptime("13:00", "%H:%M") + timedelta(minutes=30*i) for i in range(10)]  # 1 to 6 PM
    return [t.strftime("%H:%M") for t in morning + afternoon]

@slots_bp.route("/available", methods=["GET"])
def get_available_slots():
    doctor_id = request.args.get("doctor_id", type=int)
    date = request.args.get("date")  # expected: YYYY-MM-DD

    if not doctor_id or not date:
        return jsonify({"error": "doctor_id and date are required"}), 400

    conn = sqlite3.connect("hospital.db")
    cur = conn.cursor()
    cur.execute("""
        SELECT time FROM visits WHERE doctor_id = ? AND date = ?
    """, (doctor_id, date))
    booked = set(row[0] for row in cur.fetchall())

    all_slots = generate_all_slots()
    available = [s for s in all_slots if s not in booked]

    return jsonify({"available_slots": available})


@slots_bp.route("/book", methods=["POST"])
def book_slot():
    data = request.get_json()
    doctor_id = data.get("doctor_id")
    patient_id = data.get("patient_id")
    date = data.get("date")
    time = data.get("time")

    if not all([doctor_id, patient_id, date, time]):
        return jsonify({"error": "Missing fields"}), 400

    all_slots = generate_all_slots()
    if time not in all_slots:
        return jsonify({"error": "Invalid time slot"}), 400

    conn = sqlite3.connect("hospital.db")
    cur = conn.cursor()

    # Check if already booked
    cur.execute("""
        SELECT COUNT(*) FROM visits WHERE doctor_id = ? AND date = ? AND time = ?
    """, (doctor_id, date, time))
    if cur.fetchone()[0] > 0:
        return jsonify({"error": "Slot already booked"}), 409

    # Enforce 8-slot limit
    cur.execute("""
        SELECT COUNT(*) FROM visits WHERE doctor_id = ? AND date = ?
    """, (doctor_id, date))
    if cur.fetchone()[0] >= 8:
        return jsonify({"error": "Maximum slots booked for this doctor on that day"}), 403

    cur.execute("""
        INSERT INTO visits (doctor_id, patient_id, date, time)
        VALUES (?, ?, ?, ?)
    """, (doctor_id, patient_id, date, time))
    conn.commit()

    return jsonify({"message": "Appointment booked", "doctor_id": doctor_id, "patient_id": patient_id, "date": date, "time": time})
