import streamlit as st

# ---------------------------------------
# Page Configuration
# ---------------------------------------

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------------
# Custom CSS
# ---------------------------------------

st.markdown("""
<style>

.main{
    background:#F6F8FC;
}

.card{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 5px 15px rgba(0,0,0,0.08);
    border:1px solid #EAEAEA;
}

.section{
    background:white;
    padding:20px;
    border-radius:15px;
    border:1px solid #EAEAEA;
    margin-top:15px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------
# Header
# ---------------------------------------

st.title("📊 Dashboard")

st.write("Welcome back! Here's an overview of your Medical Report Analyzer.")

st.divider()

# ---------------------------------------
# Quick Actions
# ---------------------------------------

st.subheader("🚀 Quick Actions")

q1, q2, q3 = st.columns(3)

with q1:
    if st.button("📄 Upload Report", width="stretch"):
        st.switch_page("pages/2_Upload_Report.py")

with q2:
    if st.button("📈 Analytics", width="stretch"):
        st.switch_page("pages/3_Analytics.py")

with q3:
    if st.button("📜 Report History", width="stretch"):
        st.switch_page("pages/4_Report_History.py")

st.write("")

# ---------------------------------------
# Recent Activity
# ---------------------------------------

st.subheader("📁 Recent Activity")

st.info("No reports uploaded yet.")

st.write("")

# ---------------------------------------
# Latest Report
# ---------------------------------------

st.subheader("📄 Latest Report")

st.warning("No report available.")

st.write("")

# ---------------------------------------
# Health Statistics
# ---------------------------------------

st.subheader("📊 Health Statistics")

left, right = st.columns(2)

with left:
    st.info("Blood parameter charts will appear here after analysis.")

with right:
    st.info("Health score visualization will appear here.")

st.write("")

# ---------------------------------------
# Project Workflow
# ---------------------------------------

st.subheader("⚙ How It Works")

step1, step2, step3, step4 = st.columns(4)

with step1:
    st.success("1️⃣ Upload Report")

with step2:
    st.success("2️⃣ Extract Text")

with step3:
    st.success("3️⃣ AI Analysis")

with step4:
    st.success("4️⃣ Health Summary")

st.write("")

# ---------------------------------------
# Tips
# ---------------------------------------

st.subheader("💡 Tips")

st.success("""
✔ Upload PDF or Image reports

✔ AI extracts medical parameters automatically

✔ Detect abnormal values

✔ View analytics and health summary
""")

st.write("")

# ---------------------------------------
# Footer
# ---------------------------------------

st.divider()

st.caption("Medical Report Analyzer | Dashboard")

st.caption("Developed by Shravani Mahadik")