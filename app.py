import streamlit as st

# Regression coefficients
b0 = 76.451340
b1 = 0.118846

# Page title
st.title("Social Media Usage vs Academic Performance")

st.write(
    "Predict semester exam score using daily social media screen time."
)

# User input
hours = st.number_input(
    "Enter daily social media screen time (hours):",
    min_value=0.0,
    max_value=24.0,
    value=5.0,
    step=0.5
)

# Prediction
if st.button("Predict Exam Score"):

    predicted_score = b0 + b1 * hours

    st.success(
        f"Predicted Exam Score: {predicted_score:.2f}%"
    )

    st.write(
        f"Regression Equation: Y = {b0:.4f} + {b1:.4f}X"
    )