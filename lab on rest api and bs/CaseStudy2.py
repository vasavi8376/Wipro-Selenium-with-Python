from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage
doctors = {}
patients = {}
appointments = {}

doctor_id_counter = 1
patient_id_counter = 1
appointment_id_counter = 1

VALID_TOKEN = "healthcare_token_123"


#  Authentication Middleware
def check_auth():
    auth_header = request.headers.get("Authorization")
    if not auth_header or auth_header != f"Bearer {VALID_TOKEN}":
        return False
    return True


# Create Doctor
@app.route('/v1/doctors', methods=['POST'])
def create_doctor():
    global doctor_id_counter

    if not check_auth():
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json

    if not data.get("name") or data.get("experience", 0) < 0:
        return jsonify({"error": "Invalid data"}), 400

    data["doctor_id"] = doctor_id_counter
    doctors[doctor_id_counter] = data
    doctor_id_counter += 1

    return jsonify(data), 201


#  Register Patient
@app.route('/v1/patients', methods=['POST'])
def register_patient():
    global patient_id_counter

    if not check_auth():
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json

    if data.get("age", 0) < 0 or not data.get("email"):
        return jsonify({"error": "Validation error"}), 400

    # Duplicate phone check
    for patient in patients.values():
        if patient["phone"] == data.get("phone"):
            return jsonify({"error": "Duplicate phone"}), 409

    data["patient_id"] = patient_id_counter
    patients[patient_id_counter] = data
    patient_id_counter += 1

    return jsonify(data), 201


#  Book Appointment
@app.route('/v1/appointments', methods=['POST'])
def book_appointment():
    global appointment_id_counter

    if not check_auth():
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json

    if data["doctor_id"] not in doctors:
        return jsonify({"error": "Doctor not found"}), 404

    if data["patient_id"] not in patients:
        return jsonify({"error": "Patient not found"}), 404

    # Check slot conflict
    for appt in appointments.values():
        if appt["doctor_id"] == data["doctor_id"] and \
           appt["date"] == data["date"] and \
           appt["time"] == data["time"]:
            return jsonify({"error": "Slot already booked"}), 409

    data["appointment_id"] = appointment_id_counter
    data["status"] = "Booked"

    appointments[appointment_id_counter] = data
    appointment_id_counter += 1

    return jsonify(data), 201


#  View Appointment
@app.route('/v1/appointments/<int:appt_id>', methods=['GET'])
def get_appointment(appt_id):
    if not check_auth():
        return jsonify({"error": "Unauthorized"}), 401

    if appt_id not in appointments:
        return jsonify({"error": "Not found"}), 404

    return jsonify(appointments[appt_id]), 200


#  Reschedule Appointment
@app.route('/v1/appointments/<int:appt_id>', methods=['PUT'])
def reschedule_appointment(appt_id):
    if not check_auth():
        return jsonify({"error": "Unauthorized"}), 401

    if appt_id not in appointments:
        return jsonify({"error": "Not found"}), 404

    data = request.json

    # Check conflict
    for id, appt in appointments.items():
        if id != appt_id and \
           appt["doctor_id"] == appointments[appt_id]["doctor_id"] and \
           appt["date"] == data["date"] and \
           appt["time"] == data["time"]:
            return jsonify({"error": "Slot conflict"}), 409

    appointments[appt_id]["date"] = data["date"]
    appointments[appt_id]["time"] = data["time"]

    return jsonify(appointments[appt_id]), 200


#  Cancel Appointment
@app.route('/v1/appointments/<int:appt_id>', methods=['DELETE'])
def cancel_appointment(appt_id):
    if not check_auth():
        return jsonify({"error": "Unauthorized"}), 401

    if appt_id not in appointments:
        return jsonify({"error": "Gone"}), 410

    del appointments[appt_id]
    return '', 204


if __name__ == '__main__':
    app.run(debug=True)
