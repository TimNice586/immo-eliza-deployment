import streamlit as st
import numpy as np
from predict import predict

st.title("Immo Eliza Price Predictor")

region_to_provinces = {
    "Flanders": ["Antwerp", "Limburg", "East Flanders", "West Flanders", "Flemish Brabant"],
    "Wallonia": ["Hainaut", "Liège", "Namur", "Walloon Brabant", "Luxembourg"],
    "Brussels": ["Brussels"]
}

province_to_region = {
    prov: reg for reg, provs in region_to_provinces.items() for prov in provs
}

region = st.selectbox("Region", options=list(region_to_provinces.keys()))
province = st.selectbox("Province", options=region_to_provinces[region])

# If province changes → auto-update region (prevents mismatch)
auto_region = province_to_region[province]

if region != auto_region:
    st.warning(f"⚠️ Province '{province}' belongs to region '{auto_region}'. Region corrected automatically.")
    region = auto_region

# Other fields
living_area = st.number_input("Living Area (m²)", min_value=25, max_value=400000)
bedrooms = st.number_input("Bedrooms", min_value=0, max_value=50)
terrace_area = st.number_input("Terrace Area (m²)", min_value=0, max_value=150)
equiped_kitchen = st.checkbox("Equipped Kitchen")
swimming_pool = st.checkbox("Swimming Pool")
open_fire = st.checkbox("Open Fire")
terrace = st.checkbox("Terrace")
facades = st.selectbox("Facades", options=[1, 2, 3, 4])

required_cols = {
    'living_area (m²)', 'number_of_bedrooms', 'equiped_kitchen (yes:1, no:0)',
    'swimming_pool (yes:1, no:0)', 'region', 'terrace (yes:1, no:0)',
    'terrace_area (m²)', 'number_facades', 'province', 'open_fire (yes:1, no:0)',
    'type', 'garden (yes:1, no:0)', 'furnished (yes:1, no:0)',
    'state_of_building', 'subtype', 'postal_code'
}

def ensure_all_features(input_dict):
    for col in required_cols:
        if col not in input_dict:
            input_dict[col] = None  # Let model pipeline handle imputing
    return input_dict

if st.button("Predict Price"):
    input_data = {
        "living_area (m²)": int(living_area),
        "number_of_bedrooms": int(bedrooms),
        "terrace_area (m²)": int(terrace_area),
        "equiped_kitchen (yes:1, no:0)": int(equiped_kitchen),
        "swimming_pool (yes:1, no:0)": int(swimming_pool),
        "terrace (yes:1, no:0)": int(terrace),
        "region": region,
        "province": province,
        "number_facades": facades
    }
    
    input_data = ensure_all_features(input_data)
    price = predict(input_data)
    st.success(f"Estimated price: € {price:,.0f}")
