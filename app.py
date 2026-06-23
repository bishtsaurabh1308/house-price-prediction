import streamlit as st
import pandas as pd
import joblib

# Load files
model = joblib.load("house_price_model.pkl")
scaler = joblib.load("scaler.pkl")
model_columns = joblib.load("model_columns.pkl")

st.title("House Price Prediction App")

# User inputs
location = st.selectbox("Location", ["Urban", "Suburban", "Rural"])
size_sqft = st.number_input("Size sqft", min_value=400, max_value=10000, value=2500)
bedrooms = st.slider("Bedrooms", 1, 10, 3)
bathrooms = st.slider("Bathrooms", 1, 10, 2)
year_built = st.number_input("Year Built", min_value=1900, max_value=2026, value=2000)
garage = st.selectbox("Garage", ["Yes", "No"])
nearby_schools = st.slider("Nearby Schools", 0, 10, 3)
crime_rate = st.number_input("Crime Rate", min_value=0.0, max_value=10.0, value=3.0)
transport = st.slider("Transport Accessibility", 0, 8, 3)
green_space = st.slider("Green Space Availability", 0, 8, 3)
amenities = st.slider("Local Amenities", 0, 8, 3)
hoa_fees = st.number_input("HOA Fees", min_value=0, value=100)
property_tax = st.number_input("Property Tax", min_value=0, value=5000)
avg_income = st.number_input("Average Income Area", min_value=10000, value=70000)
internet = st.selectbox("Internet Availability", ["Good", "Average", "Poor"])
electricity = st.selectbox("Electricity Availability", ["Moderate","Reliable", "Unreliable"])
quality = st.selectbox("Construction Quality", ["Low", "Medium", "High"])

# Create input dataframe
input_data = pd.DataFrame({
    "Location": [location],
    "Size_sqft": [size_sqft],
    "Bedrooms": [bedrooms],
    "Bathrooms": [bathrooms],
    "Year_Built": [year_built],
    "Garage": [garage],
    "Nearby_Schools": [nearby_schools],
    "Crime_Rate": [crime_rate],
    "Transport_Accessibility": [transport],
    "Green_Space_Availability": [green_space],
    "Local_Amenities": [amenities],
    "HOA_Fees": [hoa_fees],
    "Property_Tax": [property_tax],
    "Average_Income_Area": [avg_income],
    "Internet_Availability": [internet],
    "Electricity_Availability": [electricity],
    "Construction_Quality": [quality]
})

# One-hot encoding
input_data = pd.get_dummies(input_data, drop_first=True, dtype=int)

# Match training columns
input_data = input_data.reindex(columns=model_columns, fill_value=0)

# Scale only numeric columns
num_cols = [
    'Size_sqft',
    'Bedrooms',
    'Bathrooms',
    'Year_Built',
    'Nearby_Schools',
    'Crime_Rate',
    'Transport_Accessibility',
    'Green_Space_Availability',
    'Local_Amenities',
    'HOA_Fees',
    'Property_Tax',
    'Average_Income_Area'
]

input_data[num_cols] = scaler.transform(input_data[num_cols])

# Predict
if st.button("Predict Price"):
    prediction = model.predict(input_data)
    st.success(f"Predicted House Price: {prediction[0]:,.2f}")