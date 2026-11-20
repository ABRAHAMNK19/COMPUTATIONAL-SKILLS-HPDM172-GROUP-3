# ==========================================
# Generate Lab Results Data for MySQL
# Hospital Database Coursework
# ==========================================

import random
from datetime import datetime, timedelta

# Types of laboratory tests
test_types = [
    "Blood Test",
    "Urine Test",
    "MRI Scan",
    "CT Scan",
    "X-Ray",
    "Cholesterol Test",
    "Blood Glucose Test",
    "COVID-19 Test",
    "Liver Function Test",
    "Kidney Function Test"
]

# Possible result values
result_values = [
    "Normal Range",
    "Above Normal",
    "Below Normal",
    "Positive",
    "Negative",
    "Follow Up Required"
]

# Overall interpretation
result_statuses = [
    "Normal",
    "Abnormal"
]

# Create SQL file
with open("labresults.sql", "w") as file:

    # Generate 1000 lab result records
    for _ in range(1000):

        # Select patient
        patient_id = random.randint(1, 600)

        # Select doctor
        doctor_id = random.randint(1, 100)

        # Random test type
        test_type = random.choice(test_types)

        # Random value
        result_value = random.choice(result_values)

        # Random status
        result_status = random.choice(result_statuses)

        # Random date within the last 2 years
        random_days = random.randint(0, 730)

        test_date = (
            datetime.now() - timedelta(days=random_days)
        ).strftime("%Y-%m-%d")

        # Write SQL statement
        file.write(
            f"INSERT INTO LabResults "
            f"(patient_id, doctor_id, test_type, result_value, result_status, test_date) "
            f"VALUES "
            f"({patient_id}, {doctor_id}, "
            f"'{test_type}', "
            f"'{result_value}', "
            f"'{result_status}', "
            f"'{test_date}');\n"
        )

print("Lab Results SQL file generated successfully.")