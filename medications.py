# Generate SQL inserts for Medications table

medications = [
    "Paracetamol",
    "Ibuprofen",
    "Aspirin",
    "Metformin",
    "Amoxicillin",
    "Atorvastatin",
    "Omeprazole",
    "Losartan",
    "Amlodipine",
    "Lisinopril",
    "Simvastatin",
    "Insulin",
    "Azithromycin",
    "Ciprofloxacin",
    "Prednisolone",
    "Salbutamol",
    "Warfarin",
    "Clopidogrel",
    "Codeine",
    "Tramadol",
    "Doxycycline",
    "Fluoxetine",
    "Sertraline",
    "Levothyroxine",
    "Gabapentin",
    "Furosemide",
    "Hydrochlorothiazide",
    "Ranitidine",
    "Diclofenac",
    "Naproxen"
]

with open("medications.sql", "w") as file:

    for med in medications:
        file.write(
            f"INSERT INTO Medications (MedicationName) VALUES ('{med}');\n"
        )

print("SQL file generated successfully!")