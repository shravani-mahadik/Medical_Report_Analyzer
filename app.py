import streamlit as st
import os
import json

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Medical Report Analyzer",
    page_icon="🩺",
    layout="wide"
)

REPORT_FOLDER = "reports"
LATEST_REPORT = os.path.join(REPORT_FOLDER, "latest_report.json")

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

report_count = 0
parameter_count = 0
abnormal_count = 0
health_score = "--"
patient_name = "No Report"

if os.path.exists(REPORT_FOLDER):
    report_count = len([
        f for f in os.listdir(REPORT_FOLDER)
        if f.endswith(".json") and f != "latest_report.json"
    ])

if os.path.exists(LATEST_REPORT):

    with open(LATEST_REPORT, "r") as file:
        data = json.load(file)

    summary = data["summary"]
    health_results = data["health_results"]

    patient_name = summary["Patient Name"]
    parameter_count = len(health_results)
    abnormal_count = summary["Abnormal Parameters"]
    health_score = summary["Health Score"]

# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------

st.markdown("""
<div style="
background:linear-gradient(90deg,#2563EB,#4F46E5);
padding:35px;
border-radius:18px;
color:white;
margin-bottom:25px;
">

<h1 style="margin:0;">
🩺 Medical Report Analyzer
</h1>

<p style="font-size:22px;margin-top:15px;">
Analyze Blood Reports, CBC Reports and Lab Reports using Artificial Intelligence.
</p>

</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# LIVE METRICS
# --------------------------------------------------

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("📂 Reports", report_count)

with c2:
    st.metric("🧪 Parameters", parameter_count)

with c3:
    st.metric("⚠ Alerts", abnormal_count)

with c4:
    st.metric("💚 Health Score", health_score)

st.write("")

# --------------------------------------------------
# FEATURE CARDS
# --------------------------------------------------

f1, f2, f3 = st.columns(3)

card_style = """
background:#EEF5FF;
padding:25px;
border-radius:15px;
height:200px;
border:1px solid #D6E6FF;
display:flex;
flex-direction:column;
justify-content:center;
align-items:center;
text-align:center;
"""

with f1:

    st.markdown(f"""
    <div style="{card_style}">
        <h1>📄</h1>
        <h2>Upload Reports</h2>
        <p>Upload PDF, PNG or JPG medical reports.</p>
    </div>
    """, unsafe_allow_html=True)

with f2:

    st.markdown(f"""
    <div style="{card_style}">
        <h1>🤖</h1>
        <h2>AI Analysis</h2>
        <p>Automatically detect abnormal medical values.</p>
    </div>
    """, unsafe_allow_html=True)

with f3:

    st.markdown(f"""
    <div style="{card_style}">
        <h1>📊</h1>
        <h2>Health Summary</h2>
        <p>Generate a patient-friendly health summary.</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --------------------------------------------------
# QUICK ACTIONS
# --------------------------------------------------

st.subheader("🚀 Quick Actions")

q1, q2, q3 = st.columns(3)

with q1:
    if st.button("📄 Upload Report", width="stretch"):
        st.switch_page("pages/2_Upload_Report.py")

with q2:
    if st.button("📈 View Analytics", width="stretch"):
        st.switch_page("pages/3_Analytics.py")

with q3:
    if st.button("📜 Report History", width="stretch"):
        st.switch_page("pages/4_Report_History.py")

st.divider()

# --------------------------------------------------
# LATEST REPORT
# --------------------------------------------------

st.subheader("📋 Latest Report")

if os.path.exists(LATEST_REPORT):

    left, right = st.columns([2, 1])

    with left:

        st.success(f"👤 Patient: {patient_name}")

        st.write(f"**Health Score:** {health_score}/100")

        st.write(f"**Abnormal Parameters:** {abnormal_count}")

    with right:

        st.progress(float(health_score) / 100)

else:

    st.info("No reports analyzed yet.")

st.divider()

# --------------------------------------------------
# RECENT ACTIVITY
# --------------------------------------------------

st.subheader("📁 Recent Activity")

if os.path.exists(LATEST_REPORT):

    st.success(f"Latest report analyzed for **{patient_name}**")

else:

    st.info("No recent activity.")

st.divider()

# --------------------------------------------------
# SYSTEM STATUS
# --------------------------------------------------

st.subheader("🖥 System Status")

if (
    os.path.exists("uploads")
    and os.path.exists("reports")
):
    st.success("🟢 System Ready")
else:
    st.error("🔴 System Not Ready")

st.divider()

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.caption("🏥 Medical Report Analyzer")
st.caption("Developed by Shravani Mahadik")