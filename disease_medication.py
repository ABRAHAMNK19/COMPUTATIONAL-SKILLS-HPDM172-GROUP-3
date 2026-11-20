# generate_disease_medication.py

import random

with open("disease_medication.sql", "w") as f:

    for disease_id in range(1, 21):

        meds = random.sample(range(1, 31), 3)

        for medication_id in meds:

            f.write(
                f"INSERT INTO DiseaseMedication "
                f"(disease_id, Medication_id) "
                f"VALUES ({disease_id}, {medication_id});\n"
            )

print("Disease-medication mappings generated.")