import re


def find_next_numeric(lines, start_index):
    """
    Returns the first valid numeric value after a parameter name,
    skipping units and reference ranges.
    """

    for i in range(start_index + 1, min(start_index + 6, len(lines))):

        line = lines[i].strip()

        # Skip units
        if any(unit in line.lower() for unit in ["mg", "g/", "u/", "iu", "mmol"]):
            continue

        # Skip reference ranges
        if "-" in line or "<" in line or ">" in line:
            continue

        match = re.search(r"\d+\.?\d*", line)

        if match:
            return match.group()

    return "Not Found"


def extract_parameters(text):
    """
    Extract important medical parameters from OCR text.
    """

    parameters = {
        "Patient Name": "Not Found",
        "Age": "Not Found",
        "Gender": "Not Found",
        "Hemoglobin": "Not Found",
        "RBC": "Not Found",
        "WBC": "Not Found",
        "Platelets": "Not Found",
        "Glucose": "Not Found",
        "Cholesterol": "Not Found",
        "HDL": "Not Found",
        "LDL": "Not Found",
        "Triglycerides": "Not Found",
        "Creatinine": "Not Found",
        "Blood Urea": "Not Found",
        "Uric Acid": "Not Found",
        "Total Protein": "Not Found",
        "Albumin": "Not Found",
        "Globulin": "Not Found",
        "SGOT": "Not Found",
        "SGPT": "Not Found",
        "Bilirubin": "Not Found",
    }

    lines = [line.strip() for line in text.split("\n") if line.strip()]

    parameter_map = {

        "hemoglobin": "Hemoglobin",
        "rbc": "RBC",
        "wbc": "WBC",
        "platelet": "Platelets",

        "fasting blood sugar": "Glucose",

        "total cholesterol": "Cholesterol",
        "hdl cholesterol": "HDL",
        "ldl cholesterol": "LDL",
        "triglycerides": "Triglycerides",

        "serum creatinine": "Creatinine",
        "blood urea": "Blood Urea",
        "uric acid": "Uric Acid",

        "total protein": "Total Protein",
        "albumin": "Albumin",
        "globulin": "Globulin",

        "sgot": "SGOT",
        "sgpt": "SGPT",

        "total bilirubin": "Bilirubin",
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