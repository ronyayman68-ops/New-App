# app.py
import streamlit as st

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Smart Home Energy",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- SIDEBAR ----------------

st.sidebar.title("⚡ Smart Home Energy")
st.sidebar.markdown("---")

st.sidebar.info(
    "Smart Home Energy Consumption Dashboard"
)

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Dashboard",
        "Device Analytics",
        "Predictions",
        "Data Lake",
        "Settings"
    ]
)

# ---------------- HOME PAGE ----------------

if page == "Home":

    st.title("🏠 Smart Home Energy Consumption")
    st.subheader("Data Lake Architecture System")

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Today's Usage", "0 kWh")

    with col2:
        st.metric("Monthly Cost", "$0")

    with col3:
        st.metric("Active Devices", "0")

    st.markdown("---")

    st.header("📊 System Overview")

    st.info(
        """
        This dashboard will monitor and analyze
        smart home energy consumption using
        Data Lake Architecture and Machine Learning.
        """
    )

    st.markdown("---")

    st.header("⚙️ System Architecture")

    st.code(
        """
Smart Devices
      ↓
Data Ingestion
      ↓
Data Lake
      ↓
Processing & Analytics
      ↓
Machine Learning
      ↓
Streamlit Dashboard
        """
    )

# ---------------- DASHBOARD PAGE ----------------

elif page == "Dashboard":

    st.title("📈 Energy Dashboard")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Daily Consumption")
        st.empty()

    with col2:
        st.subheader("Monthly Consumption")
        st.empty()

    st.markdown("---")

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Top Energy Devices")
        st.empty()

    with col4:
        st.subheader("Peak Usage Hours")
        st.empty()

# ---------------- DEVICE ANALYTICS ----------------

elif page == "Device Analytics":

    st.title("🔌 Device Analytics")

    devices = [
        "Air Conditioner",
        "Refrigerator",
        "TV",
        "Washing Machine",
        "Lights",
        "Heater"
    ]

    selected_device = st.selectbox(
        "Choose Device",
        devices
    )

    st.markdown("---")

    st.subheader(f"{selected_device} Analysis")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Current Usage", "0 W")

    with col2:
        st.metric("Daily Usage", "0 kWh")

    with col3:
        st.metric("Monthly Cost", "$0")

    st.markdown("---")

    st.subheader("Consumption History")
    st.empty()

# ---------------- PREDICTIONS PAGE ----------------

elif page == "Predictions":

    st.title("🤖 Energy Predictions")

    prediction_type = st.selectbox(
        "Prediction Type",
        [
            "Tomorrow Consumption",
            "Monthly Forecast",
            "Peak Usage Detection",
            "Cost Prediction"
        ]
    )

    st.markdown("---")

    st.subheader("Prediction Results")
    st.empty()

    st.markdown("---")

    st.subheader("Model Accuracy")
    st.progress(0)

# ---------------- DATA LAKE PAGE ----------------

elif page == "Data Lake":

    st.title("🗂️ Data Lake")

    st.subheader("Storage Layers")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.success("Raw Data")

    with col2:
        st.info("Processed Data")

    with col3:
        st.warning("Cleaned Data")

    with col4:
        st.error("Analytics Data")

    st.markdown("---")

    st.subheader("Uploaded Files")
    st.empty()

    st.markdown("---")

    st.subheader("ETL Pipeline")

    st.code(
        """
Extract → Transform → Load
        """
    )

# ---------------- SETTINGS PAGE ----------------

elif page == "Settings":

    st.title("⚙️ Settings")

    st.subheader("Theme")

    theme = st.selectbox(
        "Choose Theme",
        ["Dark", "Light"]
    )

    st.markdown("---")

    st.subheader("Notifications")

    st.toggle("Enable Alerts")

    st.markdown("---")

    st.subheader("System Status")

    st.success("System Ready")