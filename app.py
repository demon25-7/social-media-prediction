import streamlit as st
import streamlit as st
import matplotlib.pyplot as plt

X = [
    7, 2, 6, 2, 3, 2, 3, 6, 6, 5,
    3, 7, 8, 6, 10, 5, 2, 8, 2, 6,
    5, 3, 4, 6, 7, 5, 6, 1, 6, 5, 6
]

Y = [
    93, 63.175, 90, 70, 86, 65.93, 75, 70, 74.48, 75,
    76, 85, 75, 78, 70, 72, 85, 80, 82.46, 85,
    65, 85, 70, 75, 80, 90, 78, 85.50, 74, 71.63, 63
]

# Regression coefficients
b0 = 76.451340
b1 = 0.118846

# Scatter Plot with Regression Line

st.subheader("Scatter Plot and Regression Line")

fig, ax = plt.subplots()

ax.scatter(X, Y, label="Student Data")

Y_line = [b0 + b1 * x for x in X]

ax.plot(X, Y_line, label="Regression Line")

ax.set_xlabel("Daily Social Media Screen Time (hours)")
ax.set_ylabel("Exam Score (%)")
ax.set_title("Social Media Usage vs Academic Performance")

ax.legend()
ax.grid(True)

st.pyplot(fig)

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