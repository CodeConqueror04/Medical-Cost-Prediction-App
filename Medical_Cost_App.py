import streamlit as st
import numpy as np
import pandas as pd
import pickle

model = pickle.load(open('medical_model.pkl', 'rb'))
st.set_page_config(
    page_title=" Medical Cost Predictor (INR)", layout="centered")

st.markdown("""
    <h1 style='text-align: center; color: #1f77b4;'>💉 Medical Cost Predictor (₹ - INR)</h1>
    <p style='text-align: center; font-size:18px;'>Predict your medical insurance cost based on personal details</p>
    <p style='text-align: center; color:gray; font-size:14px;'><i>All costs shown are based on Indian healthcare estimates.</i></p>
    <hr>
""", unsafe_allow_html=True)


col1, col2 = st.columns(2)

with col1:
    age = st.number_input("🧓 Age", min_value=0, max_value=120, value=30)
    bmi = st.number_input("⚖️ BMI (Body Mass Index)",
                          min_value=10.0, max_value=50.0, value=25.0)
    children = st.number_input(
        "👶 Number of Children", min_value=0, max_value=10, value=1)
    gender = st.selectbox("🚻 Gender", ["Female", "Male"])

with col2:
    smoker = st.selectbox("🚬 Smoker", ["No", "Yes"])
    region = st.selectbox(
        "📍 Region", ["northeast", "northwest", "southeast", "southwest"])

gender = 1 if gender == "Male" else 0
smoker = 1 if smoker == "Yes" else 0
region_northwest = 1 if region == "northwest" else 0
region_southeast = 1 if region == "southeast" else 0
region_southwest = 1 if region == "southwest" else 0


st.markdown("###")
if st.button("💰 Predict Medical Cost"):
    input_df = pd.DataFrame([{
        'age': age,
        'sex': gender,
        'bmi': bmi,
        'children': children,
        'smoker': smoker,
        'region_northwest': region_northwest,
        'region_southeast': region_southeast,
        'region_southwest': region_southwest
    }])

    prediction = model.predict(input_df)[0]

    st.markdown(
        f"<h3 style='text-align: center; color: green;'>✅ Estimated Medical Cost: ₹{prediction:,.2f}</h3>",
        unsafe_allow_html=True
    )
