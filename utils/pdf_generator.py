from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from datetime import datetime




def generate_pdf(summary, health_results, output_path):

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(
        output_path,
        rightMargin=30,
        leftMargin=30,
        topMargin=30,
        bottomMargin=30
    )

    elements = []

    # ======================================================
    # TITLE
    # ======================================================

    title = Paragraph(
        "<font size=22 color='darkblue'><b>Medical Report Analyzer</b></font>",
        styles["Title"]
    )

    subtitle = Paragraph(
        "<font size=12 color='grey'>AI Powered Health Report</font>",
        styles["Heading2"]
    )

    elements.append(title)
    elements.append(subtitle)
    elements.append(Spacer(1, 0.25 * inch))

    # ======================================================
    # REPORT DATE
    # ======================================================

    date = datetime.now().strftime("%d %B %Y  %I:%M %p")

    elements.append(
        Paragraph(
            f"<b>Generated On:</b> {date}",
            styles["Normal"]
        )
    )

    elements.append(Spacer(1, 0.2 * inch))

    # ======================================================
    # PATIENT DETAILS
    # ======================================================

    patient_data = [

        ["Patient Name", summary["Patient Name"]],

        ["Age", summary["Age"]],

        ["Gender", summary["Gender"]],

        ["Health Score", f"{summary['Health Score']} / 100"],

        ["Overall Status", summary["Overall Status"]]

    ]

    patient_table = Table(
        patient_data,
        colWidths=[150, 250]
    )

    patient_table.setStyle(TableStyle([

        ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#D9EAFD")),

        ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),

        ("GRID", (0, 0), (-1, -1), 1, colors.grey),

        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),

        ("TOPPADDING", (0, 0), (-1, -1), 8),

    ]))

    elements.append(
        Paragraph(
            "<b>Patient Details</b>",
            styles["Heading2"]
        )
    )

    elements.append(patient_table)

    elements.append(Spacer(1, 0.3 * inch))

    # ======================================================
    # HEALTH SCORE
    # ======================================================

    score = summary["Health Score"]

    if score >= 90:
        score_color = "green"
    elif score >= 70:
        score_color = "orange"
    else:
        score_color = "red"

    elements.append(
        Paragraph(
            f"<font size=16 color='{score_color}'><b>Health Score : {score}/100</b></font>",
            styles["Heading2"]
        )
    )

    elements.append(Spacer(1, 0.2 * inch))

    # ======================================================
    # PARAMETERS
    # ======================================================

    elements.append(
        Paragraph(
            "<b>Medical Parameters</b>",
            styles["Heading2"]
        )
    )

    data = [["Parameter", "Value", "Status"]]
    skip_parameters = {
        "Patient Name",
        "Age",
        "Gender"
    }

    for parameter, details in health_results.items():

        if parameter in skip_parameters:
            continue

        # Skip parameters that were not detected
        if details["Value"] == "Not Found":
            continue

        status = details["Status"]

        if "Normal" in status:
            status_text = "🟢 Normal"

        elif "Low" in status:
            status_text = "🟡 Low"

        elif "High" in status:
            status_text = "🔴 High"

        elif status == "Not Available":
            status_text = "⚪ Not Available"

        elif status == "No Reference":
            status_text = "🔵 No Reference"

        else:
            status_text = status

    
        data.append([
            parameter,
            str(details["Value"]),
            status_text
        ])

    parameter_table = Table(
        data,
        colWidths=[170, 90, 140]
    )

    parameter_table.setStyle(TableStyle([

        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1E3A8A")),

        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

        ("GRID", (0, 0), (-1, -1), 1, colors.grey),

        ("BACKGROUND", (0, 1), (-1, -1), colors.whitesmoke),

        ("ALIGN", (0, 0), (-1, -1), "CENTER"),

        ("BOTTOMPADDING", (0, 0), (-1, 0), 10),

        ("TOPPADDING", (0, 1), (-1, -1), 8),

    ]))

    elements.append(parameter_table)

    elements.append(Spacer(1, 0.3 * inch))

    # ======================================================
    # RECOMMENDATIONS
    # ======================================================

    elements.append(
        Paragraph(
            "<b>Recommendations</b>",
            styles["Heading2"]
        )
    )

    for recommendation in summary["Recommendations"]:

        elements.append(
            Paragraph(
                f"• {recommendation}",
                styles["BodyText"]
            )
        )

    elements.append(Spacer(1, 0.4 * inch))

    # ======================================================
    # FOOTER
    # ======================================================

    elements.append(
        Paragraph(
            "<font color='grey'>Generated by Medical Report Analyzer</font>",
            styles["Normal"]
        )
    )

    doc.build(elements)

    return output_path