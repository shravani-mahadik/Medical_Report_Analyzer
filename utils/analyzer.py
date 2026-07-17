import re
def find_next_numeric(lines, start_index):
    """
    Returns the numeric value from the same line if present,
    otherwise searches the next few lines.
    """

    # Check current line first
    current_line = lines[start_index]

    matches = re.findall(r"\d+\.\d+|\d+", current_line)

    if matches:
        # Usually the last number on the line is the test result
        return matches[-1]

    # Otherwise check following lines
    for i in range(start_index + 1, min(start_index + 6, len(lines))):

        line = lines[i].strip().lower()

        # Skip unit/reference lines
        if any(unit in line for unit in ["mg", "g/", "iu", "mmol", "reference"]):
            continue

        match = re.search(r"\d+\.\d+|\d+", line)

        if match:
            return match.group()

        return "Not Found"


def extract_parameters(text):
    """
    Extract important medical parameters from OCR text.
    """

    parameters = {

    # Patient Details
    "Patient Name": "Not Found",
    "Age": "Not Found",
    "Gender": "Not Found",

    # CBC
    "Hemoglobin": "Not Found",
    "RBC": "Not Found",
    "WBC": "Not Found",
    "Total Leucocyte Count": "Not Found",
    "Platelets": "Not Found",
    "Platelet Count": "Not Found",

    "Neutrophils": "Not Found",
    "Lymphocytes": "Not Found",
    "Monocytes": "Not Found",
    "Eosinophils": "Not Found",
    "Basophils": "Not Found",

    "Absolute Neutrophil Count": "Not Found",
    "Absolute Lymphocyte Count": "Not Found",
    "Absolute Monocyte Count": "Not Found",
    "Absolute Eosinophil Count": "Not Found",
    "Absolute Basophil Count": "Not Found",

    "PCV": "Not Found",
    "MCV": "Not Found",
    "MCH": "Not Found",
    "MCHC": "Not Found",
    "RDW-CV": "Not Found",
    "RDW-SD": "Not Found",
    "MPV": "Not Found",
    "P-LCC": "Not Found",
    "P-LCR": "Not Found",
    "NLR": "Not Found",
    "Mentzer Index": "Not Found",

    # Sugar
    "Glucose": "Not Found",
    "PPBS": "Not Found",
    "HbA1c": "Not Found",

    # Kidney
    "Creatinine": "Not Found",
    "Blood Urea": "Not Found",
    "Uric Acid": "Not Found",

    # Liver
    "Bilirubin": "Not Found",
    "Total Bilirubin": "Not Found",
    "Direct Bilirubin": "Not Found",
    "Indirect Bilirubin": "Not Found",
    "SGOT": "Not Found",
    "SGPT": "Not Found",
    "Alkaline Phosphatase": "Not Found",
    "Albumin": "Not Found",
    "Globulin": "Not Found",
    "Total Protein": "Not Found",
    "A/G Ratio": "Not Found",

    # Lipid
    "Cholesterol": "Not Found",
    "Total Cholesterol": "Not Found",
    "HDL": "Not Found",
    "LDL": "Not Found",
    "VLDL": "Not Found",
    "Triglycerides": "Not Found",
}

    lines = [line.strip() for line in text.split("\n") if line.strip()]

    parameter_map = {

    # CBC
    "hemoglobin": "Hemoglobin",
    "hb": "Hemoglobin",

    "rbc": "RBC",

    "wbc": "WBC",
    "total leucocyte count": "Total Leucocyte Count",

    "platelets": "Platelets",
    "platelet count": "Platelet Count",

    "neutrophils": "Neutrophils",
    "lymphocytes": "Lymphocytes",
    "monocytes": "Monocytes",
    "eosinophils": "Eosinophils",
    "basophils": "Basophils",

    "absolute neutrophil count": "Absolute Neutrophil Count",
    "absolute lymphocyte count": "Absolute Lymphocyte Count",
    "absolute monocyte count": "Absolute Monocyte Count",
    "absolute eosinophil count": "Absolute Eosinophil Count",
    "absolute basophil count": "Absolute Basophil Count",

    "pcv": "PCV",
    "hematocrit": "PCV",

    "mcv": "MCV",
    "mch": "MCH",
    "mchc": "MCHC",

    "rdw-cv": "RDW-CV",
    "rdw-sd": "RDW-SD",

    "mpv": "MPV",
    "p-lcc": "P-LCC",
    "p-lcr": "P-LCR",

    "nlr": "NLR",
    "mentzer index": "Mentzer Index",

    # Sugar
    "glucose": "Glucose",
    "fasting blood sugar": "Glucose",
    "fbs": "Glucose",
    "ppbs": "PPBS",
    "hba1c": "HbA1c",

    # Kidney
    "creatinine": "Creatinine",
    "serum creatinine": "Creatinine",
    "blood urea": "Blood Urea",
    "urea": "Blood Urea",
    "uric acid": "Uric Acid",

    # Liver
    "bilirubin": "Bilirubin",
    "total bilirubin": "Total Bilirubin",
    "direct bilirubin": "Direct Bilirubin",
    "indirect bilirubin": "Indirect Bilirubin",

    "sgot": "SGOT",
    "ast": "SGOT",

    "sgpt": "SGPT",
    "alt": "SGPT",

    "alkaline phosphatase": "Alkaline Phosphatase",

    "albumin": "Albumin",
    "globulin": "Globulin",
    "total protein": "Total Protein",
    "a/g ratio": "A/G Ratio",

    # Lipid
    "cholesterol": "Cholesterol",
    "total cholesterol": "Total Cholesterol",

    "hdl": "HDL",
    "hdl cholesterol": "HDL",

    "ldl": "LDL",
    "ldl cholesterol": "LDL",

    "vldl": "VLDL",
    "vldl cholesterol": "VLDL",

    "triglycerides": "Triglycerides",
}

    for i, line in enumerate(lines):

        lower = line.lower()

        # ------------------------
        # Patient Name
        # ------------------------

        if "patient name" in lower:

            if i + 1 < len(lines):
                parameters["Patient Name"] = lines[i + 1]

            continue

        # ------------------------
        # Age & Gender
        # ------------------------

        if lower == "age":

            for j in range(i + 1, min(i + 8, len(lines))):

                if re.search(r"\d+\s*[Yy]", lines[j]):
                    parameters["Age"] = lines[j]

                elif lines[j].lower() in ["male", "female"]:
                    parameters["Gender"] = lines[j]

            continue

        # ------------------------
        # Medical Parameters
        # ------------------------

        for keyword, parameter in parameter_map.items():

            if keyword in lower:

                parameters[parameter] = find_next_numeric(lines, i)

                break

    return parameters