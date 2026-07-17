import streamlit as st
import pandas as pd
import json
import os
from datetime import datetime
from utils.pdf_generator import generate_pdf

# ----------------------------------------
# PAGE CONFIG
# ----------------------------------------

st.set_page_config(
    page_title="Report History",
    page_icon="📂",
    layout="wide"
)

st.title("📂 Medical Report History")

REPORT_FOLDER = "reports"

# ----------------------------------------
# CHECK REPORT FOLDER
# ----------------------------------------

if not os.path.exists(REPORT_FOLDER):
    st.warning("No reports found.")
    st.stop()

# ----------------------------------------
# LOAD REPORT FILES
# ----------------------------------------

report_files = sorted(
    [
        file for file in os.listdir(REPORT_FOLDER)
        if file.endswith(".json") and file != "latest_report.json"
    ],
    reverse=True
)

if not report_files:
    st.warning("No reports available.")
    st.stop()

# ----------------------------------------
# TOTAL REPORTS
# ----------------------------------------

st.metric("📂 Total Reports", len(report_files))

st.divider()

# ----------------------------------------
# LOAD HISTORY
# ----------------------------------------

history = []

for file in report_files:

    with open(os.path.join(REPORT_FOLDER, file), "r") as f:
        report = json.load(f)

    summary = report["summary"]

    history.append({
        "File": file,
        "Patient": summary["Patient Name"],
        "Age": summary["Age"],
        "Gender": summary["Gender"],
        "Health Score": summary["Health Score"],
        "Overall Status": summary["Overall Status"]
    })

history_df = pd.DataFrame(history)

# ----------------------------------------
# SEARCH
# ----------------------------------------


search = st.text_input("🔍 Search Patient")

if search:
   history_df = history_df[
    history_df["Patient"].str.contains(search, case=False, na=False)
]
# If no reports match the search
if history_df.empty:
    st.warning("🔍 No reports found for the searched patient.")
    st.stop()

# ----------------------------------------
# REPORT TABLE
# ----------------------------------------

st.subheader("📋 Previous Reports")

st.dataframe(
    history_df.drop(columns=["File"]),
    width="stretch",
    hide_index=True
)

st.divider()

# ----------------------------------------
# FRIENDLY DROPDOWN
# ----------------------------------------

display_names = {}

for file in history_df["File"]:

    name = file.replace(".json", "")
    parts = name.split("_")

    if len(parts) >= 3:

        patient = " ".join(parts[:-2])
        timestamp = parts[-2] + "_" + parts[-1]

        try:
            date = datetime.strptime(
                timestamp,
                "%Y%m%d_%H%M%S"
            )

            display = (
                f"{patient} • "
                f"{date.strftime('%d %b %Y • %I:%M %p')}"
            )

        except:
            display = patient

    else:
        display = file

    display_names[display] = file

# No reports after filtering
if not display_names:
    st.warning("🔍 No reports found for the searched patient.")
    st.stop()

selected_display = st.selectbox(
    "📂 Select Report",
    options=list(display_names.keys()),
    key="report_select"
)

selected_file = display_names.get(selected_display)

if selected_file is None:
    st.stop()


# ----------------------------------------
# LOAD REPORT
# ----------------------------------------

with open(os.path.join(REPORT_FOLDER, selected_file), "r") as f:
    report = json.load(f)

summary = report["summary"]
health_results = report["health_results"]

# ----------------------------------------
# GENERATE PDF
# ----------------------------------------

PDF_FOLDER = "pdf_reports"
os.makedirs(PDF_FOLDER, exist_ok=True)

pdf_filename = selected_file.replace(".json", ".pdf")

pdf_path = os.path.join(
    PDF_FOLDER,
    pdf_filename
)

generate_pdf(
    summary,
    health_results,
    pdf_path
)
# ----------------------------------------
# DELETE BUTTON
# ----------------------------------------

col1, col2 = st.columns(2)

with col1:

    if st.button("🗑 Delete Selected Report"):

        os.remove(os.path.join(REPORT_FOLDER, selected_file))

        st.success("Report deleted successfully!")

        st.rerun()

with col2:

    with open(pdf_path, "rb") as pdf_file:

      st.download_button(
        label="📄 Download PDF Report",
        data=pdf_file,
        file_name=pdf_filename,
        mime="application/pdf"
    )
    

st.divider()

# ----------------------------------------
# PATIENT DETAILS
# ----------------------------------------

st.subheader("🩺 Patient Details")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("👤 Patient", summary["Patient Name"])

with c2:
    st.metric("🎂 Age", summary["Age"])

with c3:
    st.metric("⚧ Gender", summary["Gender"])

st.write("")

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.metric("💯 Health Score", summary["Health Score"])

with m2:
    st.metric("🟢 Normal", summary["Normal Parameters"])

with m3:
    st.metric("🔴 Abnormal", summary["Abnormal Parameters"])

with m4:
    st.metric("🩺 Status", summary["Overall Status"])

st.divider()

# ----------------------------------------
# MEDICAL PARAMETERS
# ----------------------------------------

st.subheader("🧪 Medical Parameters")

table = []

for parameter, details in health_results.items():

    table.append({
        "Parameter": parameter,
        "Value": details["Value"],
        "Status": details["Status"]
    })

df = pd.DataFrame(table)

st.dataframe(
    df,
    width="stretch",
    hide_index=True
)

st.divider()

# ----------------------------------------
# ABNORMAL PARAMETERS
# ----------------------------------------

st.subheader("⚠️ Abnormal Parameters")

if summary["Abnormal List"]:

    for item in summary["Abnormal List"]:
        st.warning(item)

else:
    st.success("✅ No abnormal parameters detected.")

st.divider()

# ----------------------------------------
# RECOMMENDATIONS
# ----------------------------------------

st.subheader("💡 Recommendations")

for recommendation in summary["Recommendations"]:
    st.info(recommendation)