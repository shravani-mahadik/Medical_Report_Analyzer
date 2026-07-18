import streamlit as st
import pandas as pd
import json
import os
import plotly.express as px

st.set_page_config(
    page_title="Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Health Analytics Dashboard")

REPORT_FILE = "reports/latest_report.json"

# ----------------------------------------
# CHECK REPORT EXISTS
# ----------------------------------------

if not os.path.exists(REPORT_FILE):

    st.warning("⚠️ Please upload a medical report first.")

    st.info(
        "Go to **Upload Report** and analyze a report before opening Analytics."
    )

    st.stop()

# ----------------------------------------
# LOAD REPORT
# ----------------------------------------

with open(REPORT_FILE, "r") as file:

    data = json.load(file)

summary = data["summary"]
health_results = data["health_results"]

# ----------------------------------------
# TOP METRICS
# ----------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "💯 Health Score",
        summary["Health Score"]
    )

with col2:
    st.metric(
        "🟢 Normal",
        summary["Normal Parameters"]
    )

with col3:
    st.metric(
        "🔴 Abnormal",
        summary["Abnormal Parameters"]
    )

with col4:
    st.metric(
        "🩺 Overall",
        summary["Overall Status"]
    )

st.divider()

# ----------------------------------------
# ----------------------------------------
# HORIZONTAL BAR CHART
# ----------------------------------------

st.subheader("📊 Health Status Distribution")

chart_data = pd.DataFrame({
    "Status": ["🟢 Normal", "🔴 Abnormal"],
    "Count": [
        summary["Normal Parameters"],
        summary["Abnormal Parameters"]
    ]
})

fig = px.bar(
    chart_data,
    x="Count",
    y="Status",
    orientation="h",
    text="Count",
    color="Status",
    title="Normal vs Abnormal Parameters"
)

fig.update_traces(
    textposition="outside"
)

fig.update_layout(
    height=350,
    xaxis_title="Number of Parameters",
    yaxis_title="",
    showlegend=False,
    margin=dict(l=40, r=40, t=50, b=40)
)

st.plotly_chart(fig,use_container_width=True)

# ----------------------------------------
# PARAMETER TABLE
# ----------------------------------------

st.subheader("📋 Medical Parameters")

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
    use_container_width=True,
    hide_index=True
)

st.divider()

# ----------------------------------------
# ABNORMAL PARAMETERS
# ----------------------------------------

st.subheader("⚠️ Abnormal Parameters")

if summary["Abnormal List"]:

    for item in summary["Abnormal List"]:

        st.error(item)

else:

    st.success("✅ No abnormal parameters detected.")

st.divider()

# ----------------------------------------
# RECOMMENDATIONS
# ----------------------------------------

st.subheader("💡 Recommendations")

for rec in summary["Recommendations"]:

    st.info(rec)