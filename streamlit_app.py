import streamlit as st
from predict import predict

st.title("Immo Eliza Price Predictor")


living_area = st.number_input("Living Area (m²)", min_value=10, max_value=1000)
bedrooms = st.number_input("Bedrooms", min_value=0, max_value=20)

required_cols = {'living_area (m²)', 'number_of_bedrooms', 'equiped_kitchen (yes:1, no:0)', 'swimming_pool (yes:1, no:0)', 'region', 'terrace (yes:1, no:0)', 'terrace_area (m²)', 'number_facades', 'province', 'open_fire (yes:1, no:0)', 'type', 'garden (yes:1, no:0)', 'furnished (yes:1, no:0)', 'state_of_building', 'subtype', 'postal_code'} 

def ensure_all_features(input_dict):
    for col in required_cols:
        if col not in input_data:
            input_data[col] = None  #should auto use medians and so because of pipeline preproc
    return input_dict

if st.button("Predict Price"):
    input_data = {
        "living_area (m²)": living_area,
        "number_of_bedrooms": bedrooms
    }
    input_data = ensure_all_features(input_data)
    price = predict(input_data)
    st.success(f"Estimated price: € {price:,.0f}")