import streamlit as st
import pandas as pd
import joblib

# Load the model
model = joblib.load("fraud_detection_pipeline.pkl")

st.title("Fraud Detection Prediction App")
st.markdown("Please enter the transaction details and use the predict button")
st.divider()

# Input fields (Fixed 'min_value' and closing brackets)
transaction_type = st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT", "DEPOSIT"])
amount = st.number_input("Amount", min_value=0.0, value=1000.0)
oldbalanceOrg = st.number_input("Old balance (sender)", min_value=0.0, value=10000.0)
newbalanceOrig = st.number_input("New balance (sender)", min_value=0.0, value=9000.0)
oldbalanceDest = st.number_input("Old balance (receiver)", min_value=0.0, value=0.0)
newbalanceDest = st.number_input("New balance (receiver)", min_value=0.0, value=0.0)

# Everything below here is now properly indented inside the button trigger
if st.button("Predict"):
    # Fixed dictionary closing, matching variable names, and column keys
    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])

    # Predict based on the user input
    prediction = model.predict(input_data)[0]

    st.subheader(f"Prediction : '{int(prediction)}'")

    # Display results (Fixed the 'else:' colon)
    if prediction == 1:
        st.error("This transaction can be fraud")
    else:
        st.success("This is not fraud")