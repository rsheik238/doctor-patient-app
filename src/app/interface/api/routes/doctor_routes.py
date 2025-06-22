from flask import Blueprint, request, jsonify, current_app

doctor_bp = Blueprint("doctor_bp", __name__)

@doctor_bp.route("/", methods=["GET"])
def get_doctors():
    repo = current_app.container.doctor_repo
    return jsonify([doc.__dict__ for doc in repo.get_all()])

@doctor_bp.route("/", methods=["POST"])
def add_doctor():
    name = request.json.get("name")
    if not name:
        return jsonify({"error": "Name is required"}), 400
    doctor = current_app.container.doctor_repo.add(name)
    return jsonify(doctor.__dict__), 201
