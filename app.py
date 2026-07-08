import streamlit as st

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------

st.set_page_config(
    page_title="Medical Report Analyzer",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------
# CUSTOM CSS
# -------------------------------------------------

st.markdown("""
<style>

.main{
    background-color:#F6F9FC;
}

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
    padding-left:2rem;
    padding-right:2rem;
}

/* Hero */

.hero{
background:linear-gradient(90deg,#2563EB,#4F46E5);
padding:40px;
border-radius:20px;
color:white;
margin-bottom:25px;
}

.hero h1{
font-size:48px;
font-weight:bold;
margin-bottom:10px;
}

.hero p{
font-size:20px;
}

/* Cards */

.card{

background:white;
padding:25px;

border-radius:18px;

box-shadow:0px 8px 18px rgba(0,0,0,0.08);

text-align:center;

transition:0.3s;

height:230px;

}

.card:hover{

transform:translateY(-8px);

box-shadow:0px 15px 25px rgba(0,0,0,0.15);

}

/* Statistics */

.stat{

background:white;

padding:20px;

border-radius:18px;

text-align:center;

box-shadow:0px 4px 12px rgba(0,0,0,0.08);

}

/* About */

.about{

background:white;

padding:25px;

border-radius:18px;

box-shadow:0px 5px 15px rgba(0,0,0,0.08);

}

/* Footer */

.footer{

text-align:center;

color:gray;

padding:30px;

}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

with st.sidebar:

    st.image("https://img.icons8.com/color/96/stethoscope.png", width=70)

    st.title("Medical Report Analyzer")

    st.caption("AI Powered Healthcare")

    st.divider()

    st.success("🟢 System Ready")

    st.write("Upload your report from the **Upload Report** page.")

    st.divider()

    st.caption("Version 1.0")

    st.caption("Developed by")

    st.markdown("**Shravani Mahadik**")

# -------------------------------------------------
# HERO
# -------------------------------------------------

st.markdown("""

<div class="hero">

<h1>🩺 Medical Report Analyzer</h1>

<p>

Analyze Blood Reports, CBC Reports and Lab Reports using Artificial Intelligence.

</p>

</div>

""", unsafe_allow_html=True)

# -------------------------------------------------
# STATISTICS
# -------------------------------------------------

c1,c2,c3,c4=st.columns(4)

with c1:
    st.markdown("""
<div class="stat">

<h3>📂 Reports</h3>

<h1>0</h1>

</div>
""",unsafe_allow_html=True)

with c2:
    st.markdown("""
<div class="stat">

<h3>🧪 Parameters</h3>

<h1>0</h1>

</div>
""",unsafe_allow_html=True)

with c3:
    st.markdown("""
<div class="stat">

<h3>⚠ Alerts</h3>

<h1>0</h1>

</div>
""",unsafe_allow_html=True)

with c4:
    st.markdown("""
<div class="stat">

<h3>💚 Health Score</h3>

<h1>--</h1>

</div>
""",unsafe_allow_html=True)

st.write("")

# -------------------------------------------------
# FEATURES
# -------------------------------------------------

col1,col2,col3=st.columns(3)

with col1:

    st.markdown("""

<div class="card">

<h1>📄</h1>

<h2>Upload Reports</h2>

<p>

Upload PDF, PNG or JPG medical reports.

</p>

</div>

""",unsafe_allow_html=True)

with col2:

    st.markdown("""

<div class="card">

<h1>🤖</h1>

<h2>AI Analysis</h2>

<p>

Automatically detect abnormal medical values.

</p>

</div>

""",unsafe_allow_html=True)

with col3:

    st.markdown("""

<div class="card">

<h1>📈</h1>

<h2>Health Summary</h2>

<p>

Generate a simple patient-friendly report.

</p>

</div>

""",unsafe_allow_html=True)

st.write("")

# -------------------------------------------------
# QUICK ACTIONS
# -------------------------------------------------

st.subheader("🚀 Quick Actions")

a,b,c=st.columns(3)

with a:
    st.button("📄 Upload Report",use_container_width=True)

with b:
    st.button("📊 View Analytics",use_container_width=True)

with c:
    st.button("📜 Report History",use_container_width=True)

st.write("")

# -------------------------------------------------
# ABOUT
# -------------------------------------------------

st.markdown("""
<div class="about">

<h2>📘 About the Project</h2>

<p>

Medical Report Analyzer is an AI-powered healthcare assistant that extracts
medical parameters from blood reports, detects abnormal values, compares them
with reference ranges and generates an easy-to-understand health summary.

</p>

</div>

""",unsafe_allow_html=True)

st.write("")


# -------------------------------------------------
# FOOTER
# -------------------------------------------------

st.markdown("""

<div class="footer">

Medical Report Analyzer • AI/ML Internship Project

<br>

© 2026 Shravani Mahadik

</div>

""",unsafe_allow_html=True)