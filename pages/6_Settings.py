import streamlit as st
import os
import shutil

# ----------------------------------------
# PAGE CONFIG
# ----------------------------------------

st.set_page_config(
    page_title="Settings",
    page_icon="⚙️",
    layout="wide"
)

st.title("⚙️ Settings")

REPORT_FOLDER = "reports"
UPLOAD_FOLDER = "uploads"
PDF_FOLDER = "pdf_reports"

# ----------------------------------------
# HELPER FUNCTIONS
# ----------------------------------------

def folder_size(folder):
    total = 0

    if os.path.exists(folder):
        for file in os.listdir(folder):
            path = os.path.join(folder, file)

            if os.path.isfile(path):
                total += os.path.getsize(path)

    return round(total / (1024 * 1024), 2)


def file_count(folder, ignore_latest=False):

    if not os.path.exists(folder):
        return 0

    files = os.listdir(folder)

    if ignore_latest:
        files = [f for f in files if f != "latest_report.json"]

    return len(files)


# ----------------------------------------
# PROJECT STATISTICS
# ----------------------------------------

st.header("📊 Project Statistics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "📂 Reports",
        file_count(REPORT_FOLDER, ignore_latest=True)
    )

with col2:
    st.metric(
        "📄 PDFs",
        file_count(PDF_FOLDER)
    )

with col3:
    st.metric(
        "📤 Uploads",
        file_count(UPLOAD_FOLDER)
    )

with col4:
    total_size = (
        folder_size(REPORT_FOLDER)
        + folder_size(PDF_FOLDER)
        + folder_size(UPLOAD_FOLDER)
    )

    st.metric(
        "💾 Storage",
        f"{total_size} MB"
    )

st.divider()

# ----------------------------------------
# STORAGE MANAGEMENT
# ----------------------------------------

st.header("🧹 Storage Management")

col1, col2, col3 = st.columns(3)

# Delete Reports
with col1:

    if st.button("🗑 Delete All Reports"):

        if os.path.exists(REPORT_FOLDER):

            for file in os.listdir(REPORT_FOLDER):

                path = os.path.join(REPORT_FOLDER, file)

                if os.path.isfile(path):
                    os.remove(path)

        st.success("All reports deleted successfully.")

        st.rerun()

# Delete Uploads
with col2:

    if st.button("🗑 Delete Uploaded Files"):

        if os.path.exists(UPLOAD_FOLDER):

            for file in os.listdir(UPLOAD_FOLDER):

                path = os.path.join(UPLOAD_FOLDER, file)

                if os.path.isfile(path):
                    os.remove(path)

        st.success("Uploaded files deleted successfully.")

        st.rerun()

# Delete PDFs
with col3:

    if st.button("🗑 Delete PDF Reports"):

        if os.path.exists(PDF_FOLDER):

            for file in os.listdir(PDF_FOLDER):

                path = os.path.join(PDF_FOLDER, file)

                if os.path.isfile(path):
                    os.remove(path)

        st.success("PDF reports deleted successfully.")

        st.rerun()

st.divider()

# ----------------------------------------
# ABOUT PROJECT
# ----------------------------------------

st.header("ℹ️ About Project")

st.info("""
### 🏥 Medical Report Analyzer

**Version:** 1.0

**Developer:** Shravani Mahadik

**About**

This application analyzes medical reports using OCR and AI-based
parameter extraction. It evaluates health parameters, generates
recommendations, stores report history, and provides analytics.
""")

st.divider()

# ----------------------------------------
# TECHNOLOGY STACK
# ----------------------------------------

st.header("🛠 Technology Stack")

tech = [
    "🐍 Python",
    "🎈 Streamlit",
    "👁 EasyOCR",
    "📊 Pandas",
    "📄 ReportLab",
    "🖼 Pillow"
]

for item in tech:
    st.write(item)

st.divider()

# ----------------------------------------
# FOOTER
# ----------------------------------------

st.caption("© 2026 Medical Report Analyzer | Developed by Shravani Mahadik")