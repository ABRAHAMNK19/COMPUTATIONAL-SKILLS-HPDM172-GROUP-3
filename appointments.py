# ==========================================
# Generate appointment data for MySQL
# HPDM172 Hospital Database Coursework
# ==========================================

import random
from datetime import datetime, timedelta

# Possible appointment statuses
statuses = [
    "Scheduled",
    "Completed",
    "Cancelled",
    "No Show",
    "Rescheduled"
]

# Common reasons for appointments
reasons = [
    "Routine Checkup",
    "Follow-up Visit",
    "Blood Pressure Check",
    "Medication Review",
    "Diabetes Review",
    "Asthma Assessment",
    "Vaccination",
    "Lab Results Discussion",
    "Chest Pain Evaluation",
    "Flu Symptoms"
]

# Create a SQL file that will contain INSERT statements
with open("appointments.sql", "w") as file:

    # Generate 1000 appointment records
    for _ in range(1000):

        # Select a random patient ID
        patient_id = random.randint(1, 600)

        # Select a random doctor ID
        doctor_id = random.randint(1, 100)

        # Generate an appointment date
        # Some appointments will be in the past
        # and some in the future
        days = random.randint(-180, 180)

        appointment_date = (
            datetime.now() + timedelta(days=days)
        ).strftime("%Y-%m-%d %H:%M:%S")

        # Choose a random appointment reason
        reason = random.choice(reasons)

        # Choose a random status
        status = random.choice(statuses)

        # Write INSERT statement to SQL file
        file.write(
            f"INSERT INTO Appointments "
            f"(patient_id, doctor_id, appointment_date, appointment_reason, status) "
            f"VALUES "
            f"({patient_id}, {doctor_id}, "
            f"'{appointment_date}', "
            f"'{reason}', "
            f"'{status}');\n"
        )

print("Appointments SQL file generated successfully.")