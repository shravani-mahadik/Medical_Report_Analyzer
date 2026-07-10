"""
Normal reference ranges for medical parameters.
Values are based on common adult reference ranges.
"""

NORMAL_RANGES = {

    # CBC
    "Hemoglobin": (13.5, 17.5),
    "RBC": (4.5, 5.9),
    "WBC": (4000, 11000),
    "Platelets": (150000, 450000),

    # Sugar
    "Glucose": (70, 100),

    # Kidney Function
    "Creatinine": (0.70, 1.30),
    "Blood Urea": (15, 40),
    "Uric Acid": (3.5, 7.2),

    # Liver Function
    "Bilirubin": (0.2, 1.2),
    "SGOT": (10, 40),
    "SGPT": (10, 40),
    "Albumin": (3.5, 5.2),
    "Globulin": (2.0, 3.5),
    "Total Protein": (6.0, 8.3),

    # Lipid Profile
    "Cholesterol": (0, 200),
    "Triglycerides": (0, 150),
    "HDL": (40, 100),
    "LDL": (0, 130)
}