import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.title("Dopamine Receptor pEC50 Predictor")
st.markdown("Enter molecular descriptors below:")

LogP = st.number_input("LogP", value=2.3)
MW = st.number_input("Molecular Weight (MW)", min_value=1.0, value=345.2)
TPSA = st.number_input("TPSA", min_value=0.0, value=78.6)

Ring_Count = st.number_input("Ring Count", min_value=0, step=1, value=3)
Rotatable_Bonds = st.number_input("Rotatable Bonds", min_value=0, step=1, value=4)
H_Donors = st.number_input("H Donors", min_value=0, step=1, value=1)
H_Acceptors = st.number_input("H Acceptors", min_value=0, step=1, value=4)

Target_Name = st.selectbox("Target Name", ["D1", "D2", "D3", "D4", "D5"])
Assay_Type = st.selectbox("Assay Type", ["A", "B", "F"])

if st.button("Predict pEC50"):
    input_data = {
        "LogP": LogP,
        "MW": MW,
        "TPSA": TPSA,
        "Ring_Count": Ring_Count,
        "Rotatable_Bonds": Rotatable_Bonds,
        "H_Donors": H_Donors,
        "H_Acceptors": H_Acceptors,
        "Target_Name": Target_Name,
        "Assay_Type": Assay_Type
    }

    try:
        response = requests.post(API_URL, json=input_data)
        result = response.json()

        if response.status_code == 200:
            st.success(f"Predicted pEC50: **{result['pEC50']:.3f}**")
        else:
            st.error(f"API Error ({response.status_code})")
            st.write(result)

    except requests.exceptions.ConnectionError:
        st.error("Could not connect to the FastAPI server. Make sure it's running.")

