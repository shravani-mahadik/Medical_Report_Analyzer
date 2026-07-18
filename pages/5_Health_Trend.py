import streamlit as st
import os
import json
import pandas as pd
from datetime import datetime

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Health Trend",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Health Trend Analysis")
st.write(
    "Track your health progress across multiple medical reports."
)

st.divider()

# --------------------------------------------------
# REPORT FOLDER
# --------------------------------------------------

REPORT_FOLDER = "reports"

if not os.path.exists(REPORT_FOLDER):

    st.warning("No reports folder found.")
    st.stop()

# --------------------------------------------------
# LOAD REPORT FILES
# --------------------------------------------------

report_files = [

    file

    for file in os.listdir(REPORT_FOLDER)

    if file.endswith(".json")
    and file != "latest_report.json"

]

if len(report_files) == 0:

    st.warning("No reports available.")

    st.stop()

# --------------------------------------------------
# LOAD PATIENT NAMES
# --------------------------------------------------

patients = []

for file in report_files:

    try:

        with open(
            os.path.join(REPORT_FOLDER, file),
            "r"
        ) as f:

            report = json.load(f)

        patient = report["summary"]["Patient Name"]

        if patient not in patients:

            patients.append(patient)

    except:

        continue

patients.sort()

# --------------------------------------------------
# PATIENT SELECTION
# --------------------------------------------------

selected_patient = st.selectbox(

    "👤 Select Patient",

    patients

)

st.divider()

# --------------------------------------------------
# COLLECT REPORTS OF SELECTED PATIENT
# --------------------------------------------------

patient_reports = []

for file in report_files:

    try:

        with open(
            os.path.join(REPORT_FOLDER, file),
            "r"
        ) as f:

            report = json.load(f)

        summary = report["summary"]

        if summary["Patient Name"] != selected_patient:
            continue

        filename = file.replace(".json", "")

        parts = filename.split("_")

        try:

            timestamp = parts[-2] + "_" + parts[-1]

            report_date = datetime.strptime(
                timestamp,
                "%Y%m%d_%H%M%S"
            )

        except:

            report_date = datetime.now()

        patient_reports.append({

            "Date": report_date,

            "Summary": summary,

            "Parameters": report["parameters"]

        })

    except:

        continue

patient_reports = sorted(
    patient_reports,
    key=lambda x: x["Date"]
)

if len(patient_reports) == 0:

    st.warning("No reports found for selected patient.")

    st.stop()

# ==================================================
# HEALTH SCORE TREND
# ==================================================

st.header("📈 Health Score Trend")

health_data = []

for report in patient_reports:

    health_data.append({
        "Date": report["Date"],
        "Health Score": report["Summary"]["Health Score"]
    })

health_df = pd.DataFrame(health_data)

health_df = health_df.sort_values("Date")

chart = health_df.set_index("Date")

st.line_chart(chart["Health Score"])

st.write("")

# ==================================================
# HEALTH STATISTICS
# ==================================================

latest_score = health_df["Health Score"].iloc[-1]
highest_score = health_df["Health Score"].max()
lowest_score = health_df["Health Score"].min()
average_score = round(
    health_df["Health Score"].mean(),
    2
)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Current Score",
        latest_score
    )

with c2:
    st.metric(
        "Highest Score",
        highest_score
    )

with c3:
    st.metric(
        "Lowest Score",
        lowest_score
    )

with c4:
    st.metric(
        "Average Score",
        average_score
    )

st.divider()

# ==================================================
# REPORT HISTORY
# ==================================================

st.header("📋 Previous Reports")

history = []

for report in patient_reports:

    summary = report["Summary"]

    history.append({

        "Date":
        report["Date"].strftime("%d-%m-%Y %I:%M %p"),

        "Health Score":
        summary["Health Score"],

        "Overall Status":
        summary["Overall Status"],

        "Normal Parameters":
        summary["Normal Parameters"],

        "Abnormal Parameters":
        summary["Abnormal Parameters"]

    })

history_df = pd.DataFrame(history)

st.dataframe(
    history_df,
    use_container_width=True,
    hide_index=True
)

st.divider()

# ==================================================
# LATEST REPORT SUMMARY
# ==================================================

st.header("🩺 Latest Report Summary")

latest = patient_reports[-1]["Summary"]

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Patient",
        latest["Patient Name"]
    )

with col2:
    st.metric(
        "Age",
        latest["Age"]
    )

with col3:
    st.metric(
        "Gender",
        latest["Gender"]
    )

st.write("")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Health Score",
        latest["Health Score"]
    )

with col2:
    st.metric(
        "Overall Health",
        latest["Overall Status"]
    )

st.progress(
    min(
        latest["Health Score"] / 100,
        1.0
    )
)

st.divider()
# ==================================================
# PARAMETER TREND ANALYSIS
# ==================================================

st.header("🧪 Parameter Trend Analysis")

# Collect all available parameters
parameter_names = set()

for report in patient_reports:

    parameters = report["Parameters"]

    parameter_names.update(parameters.keys())

parameter_names = sorted(list(parameter_names))

if len(parameter_names) == 0:

    st.warning("No parameter data available.")

    st.stop()

selected_parameter = st.selectbox(
    "Select Medical Parameter",
    parameter_names
)

trend_data = []

for report in patient_reports:

    parameters = report["Parameters"]

    value = parameters.get(selected_parameter)

    try:

        value = float(value)

    except:

        continue

    trend_data.append({

        "Date": report["Date"],

        "Value": value

    })

if len(trend_data) == 0:

    st.info("No trend available for this parameter.")

else:

    trend_df = pd.DataFrame(trend_data)

    trend_df = trend_df.sort_values("Date")

    st.subheader(f"📈 {selected_parameter} Trend")

    chart = trend_df.set_index("Date")

    st.line_chart(chart["Value"])

    st.write("")

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.metric(
            "Current",
            round(trend_df["Value"].iloc[-1], 2)
        )

    with c2:

        st.metric(
            "Highest",
            round(trend_df["Value"].max(), 2)
        )

    with c3:

        st.metric(
            "Lowest",
            round(trend_df["Value"].min(), 2)
        )

    with c4:

        st.metric(
            "Average",
            round(trend_df["Value"].mean(), 2)
        )

    st.write("")

    first = trend_df["Value"].iloc[0]
    last = trend_df["Value"].iloc[-1]

    if last > first:

        st.success("📈 Trend: Increasing")

    elif last < first:

        st.warning("📉 Trend: Decreasing")

    else:

        st.info("➡️ Trend: Stable")

    st.write("")

    st.dataframe(
        trend_df,
        use_container_width=True,
        hide_index=True
    )

st.divider()

# ==================================================
# OVERALL INSIGHTS
# ==================================================

st.header("📊 Overall Health Insights")

latest = patient_reports[-1]["Summary"]

if latest["Health Score"] >= 90:

    st.success(
        "🎉 Excellent! Your recent health report is in a very healthy range."
    )

elif latest["Health Score"] >= 75:

    st.info(
        "👍 Your health is generally good. Continue maintaining a healthy lifestyle."
    )

elif latest["Health Score"] >= 60:

    st.warning(
        "⚠️ Some health parameters need attention. Follow your doctor's advice."
    )

else:

    st.error(
        "🚨 Multiple abnormal parameters detected. Please consult your doctor."
    )

st.write("")

st.subheader("💡 Recommendations")

for recommendation in latest["Recommendations"]:

    st.info(recommendation)

st.divider()

st.success("✅ Health Trend Analysis Completed")