def generate_health_summary(health_results):
    """
    Generate a patient-friendly health summary.
    """

    normal = 0
    abnormal = 0

    abnormal_list = []
    recommendations = []

    patient_name = "Unknown"
    age = "Unknown"
    gender = "Unknown"

    for parameter, details in health_results.items():

        value = details["Value"]
        status = details["Status"]

        # --------------------------
        # Patient Information
        # --------------------------

        if parameter == "Patient Name":
            patient_name = value

        elif parameter == "Age":
            age = value

        elif parameter == "Gender":
            gender = value

        # --------------------------
        # Health Status
        # --------------------------

        if "Normal" in status:
            normal += 1

        elif "High" in status or "Low" in status:

            abnormal += 1

            abnormal_list.append(
                f"{parameter} ({status})"
            )

            recommendations.append(
                f"Consult your doctor regarding {parameter}."
            )

    total = normal + abnormal

    if total == 0:
        health_score = 0
    else:
        health_score = round((normal / total) * 100)

    if health_score >= 90:
        overall = "🟢 Excellent"

    elif health_score >= 75:
        overall = "🟢 Good"

    elif health_score >= 50:
        overall = "🟠 Average"

    else:
        overall = "🔴 Needs Medical Attention"

    if len(recommendations) == 0:

        recommendations = [
            "Maintain a balanced diet.",
            "Exercise regularly.",
            "Drink plenty of water.",
            "Continue regular health check-ups."
        ]

    return {

        "Patient Name": patient_name,
        "Age": age,
        "Gender": gender,

        "Health Score": health_score,
        "Overall Status": overall,

        "Normal Parameters": normal,
        "Abnormal Parameters": abnormal,

        "Abnormal List": abnormal_list,

        "Recommendations": recommendations
    }