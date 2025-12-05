import streamlit as st
import numpy as np
from predict import predict

st.title("Immo Eliza Price Predictor")

#provinces are subtypes of regions
region_to_provinces = {
    "Flanders": ["Antwerp", "Limburg", "East-Flanders", "West-Flanders", "Flemish-Brabant"],
    "Wallonia": ["Hainaut", "Liège", "Namur", "Brabant-Wallon", "Luxembourg"],
    "Brussels": ["Brussels"]
}

province_to_region = {
    prov: reg for reg, provs in region_to_provinces.items() for prov in provs
}
#subtypes are part of types
type_to_subtypes = {
    "House": [
        "Residence", "Villa", "Mixed building", "Chalet",
        "Master House", "Bungalow", "Cottage", "Mansion"
    ],
    "Apartment": [
        "Apartment", "Ground Floor", "Penthouse", "Duplex", "Studio", "Triplex", "Loft"
    ]
}

subtype_to_type = {
    subtype: main_type
    for main_type, subtypes in type_to_subtypes.items()
    for subtype in subtypes
}

postal_to_province = {
    "Antwerp": range(2000, 3000),
    "East-Flanders": range(9000, 10000),
    "West-Flanders": range(8000, 9000),
    "Flemish-Brabant": list(range(1500, 2000)) + list(range(3000, 3500)),
    "Brussels": range(1000, 1300),
    "Limburg": range(3500, 4000),
    "Liège": range(4000, 5000),
    "Namur": range(5000, 6000),
    "Hainaut": list(range(6000, 6600)) + list(range(7000, 8000)),
    "Luxembourg": range(6600, 7000),
    "Brabant-Wallon": range(1300, 1500)
}
st.subheader("Place of Property")

# Postal code input with filtering / search
postal_code = st.text_input("Postal Code", placeholder="e.g. 9000")

province = None
region = None

# Detect province + region from postal code if valid
if postal_code.isdigit() and 1000 <= int(postal_code) <= 9999:
    postal_code = int(postal_code)
    province = next(
        (prov for prov, codes in postal_to_province.items() if postal_code in codes),
        None
    )
    if province:
        region = province_to_region[province]
    else:
        st.error("Unknown postal code. Please check again.")

else:
    st.info("Enter a valid Belgian postal code (1000–9999)")

# Let user toggle to override auto location
manual_override = st.checkbox("Edit location details manually")

if manual_override:
    # Manual override selectors
    region_list = list(region_to_provinces.keys())
    region = st.selectbox(
        "Region (manual override)", 
        options=region_list,
        index=region_list.index(region) if region in region_list else 0
    )
    province_list = region_to_provinces[region]
    province = st.selectbox(
        "Province (manual override)", 
        options=province_list,
        index=province_list.index(province) if province in province_list else 0
    )
else:
    if region and province:
        st.success(f"Located in: {region} → {province}")
    else:
        st.warning("Province & Region will be set once the postal code is valid.")
st.subheader("Types of Property")

type_list = list(type_to_subtypes.keys())
property_type = st.selectbox("Type", options=type_list)

subtype_list = type_to_subtypes[property_type]
subtype = st.selectbox("Subtype", options=subtype_list)

# Auto-correct type if subtype changed afterwards
correct_type = subtype_to_type[subtype]
if property_type != correct_type:
    st.warning(f"Subtype '{subtype}' belongs to type '{correct_type}'. Type corrected automatically.")
    property_type = correct_type

st.subheader("Property details")
# Other fields
living_area = st.number_input("Living Area (m²)", min_value=25, max_value=400000)
bedrooms = st.number_input("Bedrooms", min_value=0, max_value=50)
terrace_area = st.number_input("Terrace Area (m²)", min_value=0, max_value=150)
equiped_kitchen = st.checkbox("Equipped Kitchen")
swimming_pool = st.checkbox("Swimming Pool")
open_fire = st.checkbox("Open Fire")
terrace = st.checkbox("Terrace")
garden = st.checkbox("Garden")
furnished = st.checkbox("Furnished")
state_of_building = st.selectbox("State", options=['Excellent','To be renovated',
        'New','Normal','Fully renovated',
        'To renovate','Under construction','To demolish',
         'To restore'])
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
        "number_facades": facades,
        "open_fire (yes:1, no:0)": open_fire,
        "type": property_type,
        "subtype": subtype,
        "garden (yes:1, no:0)": garden,
        "furnished (yes:1, no:0)": furnished,
        "state_of_building": state_of_building 
    }
    
    input_data = ensure_all_features(input_data)
    price = predict(input_data)
    st.success(f"Estimated price: € {price:,.0f}")
