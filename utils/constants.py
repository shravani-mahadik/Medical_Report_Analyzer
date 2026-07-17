"""
Normal reference ranges for medical parameters.
Values are based on common adult reference ranges.
"""

NORMAL_RANGES = {

    # =====================================================
    # COMPLETE BLOOD COUNT (CBC)
    # =====================================================

    "Hemoglobin": (13.5, 17.5),          # g/dL
    "RBC": (4.5, 5.9),                   # million/µL
    "WBC": (4000, 11000),                # /µL
    "Total Leucocyte Count": (4.0, 10.0),# x10³/µL
    "Platelets": (150000, 450000),       # /µL
    "Platelet Count": (150, 410),        # x10³/µL

    # Differential Leucocyte Count
    "Neutrophils": (40, 80),             # %
    "Lymphocytes": (20, 40),             # %
    "Monocytes": (2, 10),                # %
    "Eosinophils": (1, 6),               # %
    "Basophils": (0, 1),                 # %

    # Absolute Counts
    "Absolute Neutrophil Count": (2.0, 7.5),
    "Absolute Lymphocyte Count": (1.0, 4.0),
    "Absolute Monocyte Count": (0.2, 1.0),
    "Absolute Eosinophil Count": (0.02, 0.5),
    "Absolute Basophil Count": (0.00, 0.30),

    # RBC Indices
    "PCV": (40, 50),
    "Hematocrit": (40, 50),
    "MCV": (83, 101),
    "MCH": (27, 32),
    "MCHC": (31.5, 34.5),
    "RDW-CV": (11.5, 14.5),
    "RDW-SD": (39, 46),
    "MPV": (7.5, 12.0),

    # Platelet Indices
    "P-LCC": (30, 90),
    "P-LCR": (11, 45),

    # Ratios
    "NLR": (0.5, 3.0),
    "Neutrophil-Lymphocyte Ratio": (0.5, 3.0),
    "Mentzer Index": (0, 13),

    # =====================================================
    # BLOOD SUGAR
    # =====================================================

    "Glucose": (70, 100),
    "Fasting Blood Sugar": (70, 100),
    "FBS": (70, 100),
    "PPBS": (70, 140),
    "HbA1c": (4.0, 5.6),

    # =====================================================
    # KIDNEY FUNCTION TEST (KFT)
    # =====================================================

    "Creatinine": (0.70, 1.30),
    "Serum Creatinine": (0.70, 1.30),
    "Blood Urea": (15, 40),
    "Urea": (15, 40),
    "Uric Acid": (3.5, 7.2),

    # =====================================================
    # LIVER FUNCTION TEST (LFT)
    # =====================================================

    "Bilirubin": (0.2, 1.2),
    "Total Bilirubin": (0.2, 1.2),
    "Direct Bilirubin": (0.0, 0.3),
    "Indirect Bilirubin": (0.2, 0.9),

    "SGOT": (10, 40),
    "AST": (10, 40),

    "SGPT": (10, 40),
    "ALT": (10, 40),

    "Alkaline Phosphatase": (30, 120),

    "Albumin": (3.5, 5.2),
    "Globulin": (2.0, 3.5),
    "Total Protein": (6.0, 8.3),
    "A/G Ratio": (1.0, 2.0),

    # =====================================================
    # LIPID PROFILE
    # =====================================================

    "Cholesterol": (0, 200),
    "Total Cholesterol": (0, 200),

    "Triglycerides": (0, 150),

    "HDL": (40, 100),
    "HDL Cholesterol": (40, 100),

    "LDL": (0, 130),
    "LDL Cholesterol": (0, 130),

    "VLDL": (10, 40),
    "VLDL Cholesterol": (10, 40)
}