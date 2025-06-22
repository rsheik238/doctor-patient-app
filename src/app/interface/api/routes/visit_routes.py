from flask import Blueprint, request, jsonify, current_app

visit_bp = Blueprint("visit_bp", __name__)

@visit_bp.route("/", methods=["GET"])
def get_visits():
    repo = current_app.container.visit_repo
    return jsonify([v.__dict__ for v in repo.get_all()])

@visit_bp.route("/", methods=["POST"])
def schedule_visit():
    data = request.get_json()
    doctor = data.get("doctor")
    patient = data.get("patient")
    date = data.get("date")
    time = data.get("time")
    if not all([doctor, patient, date, time]):
        return jsonify({"error": "All fields required"}), 400
    visit = current_app.container.visit_repo.add(doctor, patient, date, time)
    return jsonify(visit.__dict__), 201
