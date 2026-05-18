import streamlit as st
import pandas as pd
import numpy as np

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Smart Home Energy",
    page_icon="⚡",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #0F172A;
    color: white;
}

section[data-testid="stSidebar"] {
    background-color: #111827;
}

h1, h2, h3 {
    color: #00E5FF;
}

div[data-testid="metric-container"] {
    background-color: #1E293B;
    border: 1px solid #334155;
    padding: 15px;
    border-radius: 15px;
}

.stButton>button {
    background-color: #00E5FF;
    color: black;
    border-radius: 10px;
    border: none;
    padding: 10px 20px;
    font-weight: bold;
}

.stButton>button:hover {
    background-color: #7C3AED;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.title("⚡ Smart Home")

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Dashboard",
        "Devices",
        "Predictions",
        "Data Lake",
        "Settings"
    ]
)

# ---------------------------------------------------
# FAKE DATA
# ---------------------------------------------------

hours = np.arange(24)

energy = np.random.randint(
    20,
    100,
    size=24
)

df = pd.DataFrame({
    "Hour": hours,
    "Energy": energy
})

# ---------------------------------------------------
# HOME PAGE
# ---------------------------------------------------

if page == "Home":

    st.title("🏠 Smart Home Energy System")

    st.subheader(
        "Data Lake Architecture Dashboard"
    )

    st.markdown("---")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Today's Usage",
            "145 kWh",
            "+12%"
        )

    with col2:
        st.metric(
            "Monthly Cost",
            "$320",
            "-5%"
        )

    with col3:
        st.metric(
            "Active Devices",
            "12"
        )

    with col4:
        st.metric(
            "Efficiency",
            "89%"
        )

    st.markdown("---")

    st.header("📊 System Overview")

    st.info(
        """
        This dashboard monitors smart home
        energy consumption using Data Lake
        Architecture and AI Analytics.
        """
    )

    st.markdown("---")

    st.header("⚙️ System Architecture")

    st.code("""
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
""")

# ---------------------------------------------------
# DASHBOARD PAGE
# ---------------------------------------------------

elif page == "Dashboard":

    st.title("📈 Energy Dashboard")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Daily Energy Usage")

        st.line_chart(
            df.set_index("Hour")
        )

    with col2:

        st.subheader("Energy Distribution")

        device_data = pd.DataFrame({
            "Device": [
                "AC",
                "Lights",
                "TV",
                "Heater",
                "Fridge"
            ],
            "Usage": [
                40,
                15,
                10,
                20,
                15
            ]
        })

        st.bar_chart(
            device_data.set_index("Device")
        )

    st.markdown("---")

    col3, col4 = st.columns(2)

    with col3:

        st.subheader("Peak Usage Hours")

        st.area_chart(
            df.set_index("Hour")
        )

    with col4:

        st.subheader("System Status")

        st.success(
            "All devices are working normally"
        )

        st.info(
            "No unusual energy spikes detected"
        )

# ---------------------------------------------------
# DEVICES PAGE
# ---------------------------------------------------

elif page == "Devices":

    st.title("🔌 Smart Devices")

    devices = {
        "Air Conditioner": "ON",
        "Lights": "ON",
        "TV": "OFF",
        "Heater": "ON",
        "Refrigerator": "ON",
        "Washing Machine": "OFF"
    }

    st.markdown("---")

    for device, status in devices.items():

        col1, col2, col3 = st.columns([3, 1, 1])

        with col1:
            st.subheader(device)

        with col2:
            st.write(f"Status: {status}")

        with col3:
            st.button(
                "Control",
                key=device
            )

        st.markdown("---")

# ---------------------------------------------------
# PREDICTIONS PAGE
# ---------------------------------------------------

elif page == "Predictions":

    st.title("🤖 AI Predictions")

    prediction = st.selectbox(
        "Choose Prediction",
        [
            "Tomorrow Usage",
            "Monthly Forecast",
            "Peak Hour Detection",
            "Cost Prediction"
        ]
    )

    st.markdown("---")

    st.subheader("Prediction Result")

    st.info(
        "Predicted energy consumption tomorrow: 152 kWh"
    )

    st.markdown("---")

    st.subheader("Forecast Chart")

    forecast = pd.DataFrame({
        "Day": np.arange(1, 8),
        "Prediction": np.random.randint(
            120,
            180,
            7
        )
    })

    st.line_chart(
        forecast.set_index("Day")
    )

# ---------------------------------------------------
# DATA LAKE PAGE
# ---------------------------------------------------

elif page == "Data Lake":

    st.title("🗂️ Data Lake")

    st.markdown("---")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.success("Raw Data")

    with col2:
        st.info("Processed Data")

    with col3:
        st.warning("Cleaned Data")

    with col4:
        st.error("Analytics")

    st.markdown("---")

    st.subheader("ETL Pipeline")

    st.code("""
Extract → Transform → Load
""")

    st.markdown("---")

    st.subheader("Pipeline Status")

    st.progress(75)

# ---------------------------------------------------
# SETTINGS PAGE
# ---------------------------------------------------

elif page == "Settings":

    st.title("⚙️ Settings")

    dark_mode = st.toggle(
        "Dark Mode",
        value=True
    )

    alerts = st.toggle(
        "Enable Alerts",
        value=True
    )

    notifications = st.toggle(
        "Push Notifications"
    )

    st.markdown("---")

    st.success("System Ready")