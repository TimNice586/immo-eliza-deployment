import streamlit as st
from predict import predict

st.title("Immo Eliza Price Predictor")

living_area = st.number_input("Living Area (m²)", min_value=10, max_value=1000)
bedrooms = st.number_input("Bedrooms", min_value=0, max_value=20)

if st.button("Predict Price"):
    input_data = {
        "LivingArea": living_area,
        "Bedrooms": bedrooms
    }
    price = predict(input_data)
    st.success(f"Estimated price: € {price:,.0f}")