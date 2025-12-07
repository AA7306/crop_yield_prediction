import streamlit as st
import pickle
import pandas as pd
import numpy as np

# =========================
# SESSION STATE INIT (FOR RESET)
# =========================
if "init" not in st.session_state:
    st.session_state.init = True

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Crop Yield Predictor",
    page_icon="🌾",
    layout="centered"
)

# =========================
# LOAD MODEL & FEATURES
# =========================
model = pickle.load(open("crop_yield_model.pkl", "rb"))
X_train_cols = pickle.load(open("model_features.pkl", "rb"))

# =========================
# LOAD YIELD THRESHOLDS (WITH FALLBACK)
# =========================
try:
    low_threshold, high_threshold = pickle.load(open("yield_thresholds.pkl", "rb"))
except:
    low_threshold = 2.0
    high_threshold = 5.0

# =========================
# HELPER FUNCTIONS
# =========================
def classify_yield(value):
    if value < low_threshold:
        return "🔴 Low Yield"
    elif value < high_threshold:
        return "🟡 Medium Yield"
    else:
        return "🟢 High Yield"


def yield_advice(label):
    if "Low" in label:
        return "⚠️ Yield is low. Improve irrigation, fertilizer usage, or crop selection."
    elif "Medium" in label:
        return "✅ Yield is moderate. Optimize water, temperature, and soil conditions."
    else:
        return "🚀 High yield expected! Farming practices are well optimized."


# =========================
# APP TITLE
# =========================
st.title("🌾 Crop Yield Prediction System")
st.markdown("Predict crop yield using Machine Learning")
st.divider()

# =========================
# 🌍 ENVIRONMENTAL CONDITIONS
# =========================
st.subheader("🌍 Environmental Conditions")

Region = st.selectbox("Region", ["West", "East", "North", "South"], key="Region")
Weather_Condition = st.selectbox("Weather Condition", ["Sunny", "Cloudy", "Rainy"], key="Weather")
Rainfall_mm = st.number_input("Rainfall (mm)", min_value=0.0, key="Rainfall")
Temperature_Celsius = st.number_input("Temperature (°C)", min_value=0.0, key="Temp")

st.divider()

# =========================
# 🌱 CROP DETAILS
# =========================
st.subheader("🌱 Crop Details")

Soil_Type = st.selectbox("Soil Type", ["Sandy", "Loamy", "Clay"], key="Soil")
Crop = st.selectbox("Crop", ["Wheat", "Rice", "Cotton", "Maize"], key="Crop")
Days_to_Harvest = st.number_input("Days to Harvest", min_value=1, key="Days")

st.divider()

# =========================
# 🚜 FARMING PRACTICES
# =========================
st.subheader("🚜 Farming Practices")

Fertilizer_Used = st.selectbox("Fertilizer Used", [True, False], key="Fertilizer")
Irrigation_Used = st.selectbox("Irrigation Used", [True, False], key="Irrigation")

st.divider()

# =========================
# 🚀 PREDICTION
# =========================
if st.button("🚀 Predict Yield"):

    input_data = {
        'Region': [Region],
        'Soil_Type': [Soil_Type],
        'Crop': [Crop],
        'Rainfall_mm': [Rainfall_mm],
        'Temperature_Celsius': [Temperature_Celsius],
        'Fertilizer_Used': [Fertilizer_Used],
        'Irrigation_Used': [Irrigation_Used],
        'Weather_Condition': [Weather_Condition],
        'Days_to_Harvest': [Days_to_Harvest]
    }

    input_df = pd.DataFrame(input_data)

    # Convert boolean to int
    for col in ['Fertilizer_Used', 'Irrigation_Used']:
        input_df[col] = input_df[col].astype(int)

    categorical_cols = [
        'Region', 'Soil_Type', 'Crop',
        'Fertilizer_Used', 'Irrigation_Used',
        'Weather_Condition'
    ]

    input_processed = pd.get_dummies(
        input_df, columns=categorical_cols, drop_first=True
    )

    input_aligned = input_processed.reindex(
        columns=X_train_cols, fill_value=0
    )

    result = model.predict(input_aligned)[0]

    label = classify_yield(result)
    advice = yield_advice(label)

    # =========================
    # 📦 OUTPUT CARD
    # =========================
    st.subheader("📦 Prediction Result")

    st.success(f"🌾 **Predicted Crop Yield:** {result:.2f} tons / hectare")
    st.info(f"📊 **Yield Category:** {label}")
    st.warning(advice)

    # =========================
    # 📈 VISUAL BAR INDICATOR
    # =========================
    progress_value = min(float(result / (high_threshold * 1.2)), 1.0)
    st.progress(progress_value)




