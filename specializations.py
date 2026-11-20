# generate_specializations.py

import random

with open("specializations.sql", "w") as f:

    for doctor_id in range(1, 101):

        disease_id = random.randint(1, 20)

        f.write(
            f"INSERT INTO DoctorSpecializations "
            f"(doctor_id, disease_id) "
            f"VALUES ({doctor_id}, {disease_id});\n"
        )

print("Specialization data generated.")