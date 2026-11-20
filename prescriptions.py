import random
from datetime import datetime, timedelta

NUM_PRESCRIPTIONS = 500

with open("prescriptions.sql", "w") as file:

    for i in range(NUM_PRESCRIPTIONS):

        patient_id = random.randint(1, 600)
        doctor_id = random.randint(1, 100)
        medication_id = random.randint(1, 30)

        random_days = random.randint(0, 730)
        prescription_date = (
            datetime.now() - timedelta(days=random_days)
        ).strftime("%Y-%m-%d")

        file.write(
            f"INSERT INTO Prescriptions "
            f"(patient_id, doctor_id, Medication_id, prescription_date) "
            f"VALUES "
            f"({patient_id}, {doctor_id}, {medication_id}, '{prescription_date}');\n"
        )

print("500 prescriptions generated successfully!")