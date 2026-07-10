import streamlit as st
from PIL import Image
import pandas as pd
import os

from utils.image_reader import read_image
from utils.pdf_reader import read_pdf
from utils.analyzer import extract_parameters
from utils.health_checker import check_health
from utils.summary import generate_health_summary

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Upload Report",
    page_icon="📄",
    layout="wide"
)

# ---------------------------------------------------
# CREATE UPLOAD FOLDER
# ---------------------------------------------------

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ---------------------------------------------------
# PAGE TITLE
# ---------------------------------------------------

st.title("📄 Upload Medical Report")

st.write(
    "Upload your Blood Report, CBC Report, or any Medical Report for AI-powered analysis."
)

st.divider()

# ---------------------------------------------------
# FILE UPLOADER
# ---------------------------------------------------

uploaded_file = st.file_uploader(
    "Choose your Medical Report",
    type=["pdf", "png", "jpg", "jpeg"]
)

# ---------------------------------------------------
# PROCESS FILE
# ---------------------------------------------------

if uploaded_file is not None:

    # Save uploaded file

    save_path = os.path.join(
        UPLOAD_FOLDER,
        uploaded_file.name
    )

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("✅ Report uploaded successfully!")

    # ------------------------------------------------
    # FILE INFORMATION
    # ------------------------------------------------

    st.subheader("📋 File Information")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Filename", uploaded_file.name)

    with c2:
        st.metric(
            "File Size",
            f"{uploaded_file.size / 1024:.2f} KB"
        )

    with c3:
        st.metric(
            "File Type",
            uploaded_file.type
        )

    st.divider()

    # ------------------------------------------------
    # PREVIEW
    # ------------------------------------------------

    st.subheader("🖼 Report Preview")

    if uploaded_file.type.startswith("image"):

        image = Image.open(uploaded_file)

        st.image(
            image,
            caption="Uploaded Medical Report",
            use_container_width=True
        )

        extracted_text = read_image(save_path)

    else:

        st.info("📄 PDF uploaded successfully.")

        extracted_text = read_pdf(save_path)

    # ------------------------------------------------
    # OCR TEXT (Developer Mode)
    # ------------------------------------------------

    with st.expander("📄 View OCR Text (Developer Mode)"):

        st.text_area(
            "OCR Output",
            extracted_text,
            height=250
        )

    # ------------------------------------------------
    # PARAMETER EXTRACTION
    # ------------------------------------------------

    parameters = extract_parameters(extracted_text)

    # ------------------------------------------------
    # HEALTH CHECK
    # ------------------------------------------------

    health_results = check_health(parameters)

    summary = generate_health_summary(health_results)

    # ------------------------------------------------
    # MEDICAL ANALYSIS TABLE
    # ------------------------------------------------

    st.divider()

    st.subheader("🩺 Medical Analysis")

    table_data = []

    for parameter, details in health_results.items():

        table_data.append({

            "Parameter": parameter,

            "Value": details["Value"],

            "Status": details["Status"]

        })

    df = pd.DataFrame(table_data)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

   
    # ----------------------------
    # HEALTH SUMMARY
    # ----------------------------

    st.divider()

    st.subheader("🩺 Patient Health Summary")

    info1, info2, info3 = st.columns(3)

    with info1:
        st.metric("👤 Patient", summary["Patient Name"])

    with info2:
        st.metric("🎂 Age", summary["Age"])

    with info3:
        st.metric("⚧ Gender", summary["Gender"])

    st.write("")

    score_col, status_col = st.columns(2)

    with score_col:

        st.metric(
            "💯 Health Score",
            f"{summary['Health Score']} / 100"
        )

        progress = min(max(summary["Health Score"]/100,0),1)

        st.progress(progress)

    with status_col:

        st.metric(
            "🩺 Overall Health",
            summary["Overall Status"]
        )

    st.write("")

    st.subheader("📊 Report Statistics")

    stat1, stat2 = st.columns(2)

    with stat1:
        st.success(
            f"🟢 Normal Parameters : {summary['Normal Parameters']}"
        )

    with stat2:
        st.error(
            f"🔴 Abnormal Parameters : {summary['Abnormal Parameters']}"
        )

    st.write("")

    st.subheader("⚠️ Abnormal Parameters")

    if summary["Abnormal List"]:

        for item in summary["Abnormal List"]:
            st.warning(item)

    else:
        st.success("✅ No abnormal parameters detected.")

    st.write("")

    st.subheader("💡 Recommendations")

    for recommendation in summary["Recommendations"]:
        st.info(recommendation)

else:

    st.info("⬆️ Please upload a PDF, JPG, JPEG or PNG medical report.")