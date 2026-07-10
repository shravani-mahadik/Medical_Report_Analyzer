from utils.health_checker import check_health

parameters = {
    "Glucose": "70",
    "Creatinine": "0.98",
    "Cholesterol": "180",
    "Triglycerides": "132",
    "HDL": "45",
    "LDL": "109",
    "Hemoglobin": "12.1",
    "Platelets": "620000"
}

results = check_health(parameters)

for parameter, details in results.items():

    print(
        f"{parameter:20} "
        f"{details['Value']:10} "
        f"{details['Status']}"
    )
    