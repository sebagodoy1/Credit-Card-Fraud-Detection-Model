import pickle
import numpy as np
import streamlit as st

# Title of the application
st.title("Credit Card Fraud Detection Model")

# Image (if it's in the same folder as this file)
st.image(("imagen.png"), use_column_width=True)

# User input for features
input_df = st.text_input("Please provide all the required feature details (separated by commas):")

# Submit button
submit = st.button("Submit")

@st.cache_resource
def load_model():
    return pickle.load(open('model.pkl', 'rb'))

# Load the model
model = load_model()


# Function to make the prediction
def predict_fraud(input_data):
    features = np.array(input_data.split(','), dtype=np.float64).reshape(1, -1)
    prediction = model.predict(features)
    return prediction[0]

# Perform prediction if the button is pressed
if submit:
    if input_df:
        prediction = predict_fraud(input_df)
        if prediction == 0:
            st.write("Legitimate Transaction")
        else:
            st.write("Fraudulent Transaction")
    else:
        st.warning("Please provide valid feature details.")