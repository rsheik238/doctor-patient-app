from flask import Blueprint, request, jsonify, current_app

patient_bp = Blueprint("patient_bp", __name__)

@patient_bp.route("/", methods=["GET"])
def get_patients():
    repo = current_app.container.patient_repo
    return jsonify([p.__dict__ for p in repo.get_all()])

@patient_bp.route("/", methods=["POST"])
def add_patient():
    name = request.json.get("name")
    if not name:
        return jsonify({"error": "Name is required"}), 400
    patient = current_app.container.patient_repo.add(name)
    return jsonify(patient.__dict__), 201
