import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="Upload Report", page_icon="📄", layout="wide")

st.title("📄 Upload Medical Report")

st.write("Upload a PDF or an image of your medical report.")

uploaded_file = st.file_uploader(
    "Choose your report",
    type=["pdf", "png", "jpg", "jpeg"]
)

if uploaded_file:

    os.makedirs("uploads", exist_ok=True)

    save_path = os.path.join("uploads", uploaded_file.name)

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("✅ File uploaded successfully!")

    st.write("### File Information")

    st.write(f"**Filename:** {uploaded_file.name}")
    st.write(f"**File Size:** {uploaded_file.size/1024:.2f} KB")
    st.write(f"**File Type:** {uploaded_file.type}")

    if uploaded_file.type.startswith("image"):

        image = Image.open(uploaded_file)

        st.image(image, caption="Uploaded Report", use_container_width=True)

    else:

        st.info("PDF uploaded successfully. PDF preview will be added next.")