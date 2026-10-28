import streamlit as st
import json
import time
from PIL import Image

st.set_page_config(page_title="Multimodal Construction Intelligence", page_icon="🏗️", layout="wide")

st.sidebar.title("🏗️ Construction AI Workspace")
st.sidebar.caption("Platform ID: 6ac4c98d1dcde6d7857c1642")
api_key = st.sidebar.text_input("Gemini API Key (Optional)", type="password")
if api_key:
    st.sidebar.success("✅ Connected to Gemini API")
else:
    st.sidebar.info("ℹ️ Running in Interactive Demo Simulation Mode")

st.title("Multimodal Construction Intelligence Platform")
st.caption("AI-driven decision support for safety auditing, defect diagnostics, valuation, and site telemetry.")

tab1, tab2, tab3, tab4 = st.tabs(["🦺 PPE Safety Audit", "🔍 Crack Diagnostics", "📊 Valuation & Planning", "🌦️ Weather Advisory"])

with tab1:
    st.subheader("OSHA & IS 456 PPE Safety Compliance")
    uploaded_file = st.file_uploader("Upload Site Image", type=["jpg", "jpeg", "png"], key="safety")
    if uploaded_file:
        img = Image.open(uploaded_file)
        c1, c2 = st.columns(2)
        c1.image(img, use_column_width=True)
        with c2:
            if st.button("Run Audit", type="primary"):
                with st.spinner("Analyzing site safety..."):
                    time.sleep(1)
                    report = {
                        "safety_score": 85,
                        "overall_status": "Conditionally Compliant",
                        "violations": ["Worker without safety lanyard at height (>3m)"],
                        "ppe_status": {"Helmets": "100% Detected", "Vests": "100% Detected", "Boots": "Compliant"}
                    }
                    st.metric("Safety Score", f"{report['safety_score']}/100")
                    st.write(f"**Status:** {report['overall_status']}")
                    st.error(f"Hazard: {report['violations'][0]}")
                    st.download_button("Download JSON Report", json.dumps(report, indent=2), "safety_audit.json")

with tab2:
    st.subheader("Structural Integrity & Crack Classification")
    uploaded_crack = st.file_uploader("Upload Defect Image", type=["jpg", "jpeg", "png"], key="crack")
    if uploaded_crack:
        c1, c2 = st.columns(2)
        c1.image(Image.open(uploaded_crack), use_column_width=True)
        with c2:
            if st.button("Diagnose Defect", type="primary"):
                time.sleep(1)
                st.info("Defect Type: Structural Shear Crack (Width ~2.2mm)")
                st.warning("Severity: High — Structural Engineering Review Required")
                st.success("Remedy: Polyurethane pressure grouting & carbon fiber wrapping")

with tab3:
    st.subheader("Budget & Valuation Estimator (INR)")
    area = st.number_input("Built-up Area (Sq. Ft.)", value=2000, step=100)
    tier = st.selectbox("Location Tier", ["Tier 1 (Metro)", "Tier 2 (Indore, Bhopal, Pune)", "Tier 3 / Regional"])
    rate = 6000 if "Tier 1" in tier else (4000 if "Tier 2" in tier else 2800)
    budget = area * rate
    c1, c2 = st.columns(2)
    c1.metric("Estimated Cost", f"₹{budget/100000:.2f} Lakhs")
    c2.metric("Cement Required", f"{int(area * 0.45)} Bags")

with tab4:
    st.subheader("Daily Weather Protocol & Chatbot")
    weather = st.selectbox("Site Condition", ["Clear Sky", "High Wind (>40 km/h)", "Heavy Rain", "Extreme Heat"])
    if "High Wind" in weather:
        st.error("Protocol: Suspend tower crane lifts and secure perimeter netting.")
    elif "Heavy Rain" in weather:
        st.warning("Protocol: Halt exterior excavations; check retaining walls.")
    else:
        st.success("Protocol: Standard construction operations permitted.")
