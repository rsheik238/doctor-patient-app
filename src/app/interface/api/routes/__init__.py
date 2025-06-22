from .doctor_routes import doctor_bp
from .patient_routes import patient_bp
from .visit_routes import visit_bp

blueprints = [
    (doctor_bp, "/doctors"),
    (patient_bp, "/patients"),
    (visit_bp, "/visits"),
]
