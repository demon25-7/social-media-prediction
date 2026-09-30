import streamlit as st
import matplotlib.pyplot as plt

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Social Media & Academic Performance",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# DATA
# --------------------------------------------------

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

N = len(X)

# --------------------------------------------------
# REGRESSION CALCULATIONS
# --------------------------------------------------

sumX = sum(X)
sumY = sum(Y)

sumX2 = sum(x * x for x in X)
sumY2 = sum(y * y for y in Y)

sumXY = sum(X[i] * Y[i] for i in range(N))

numerator = N * sumXY - sumX * sumY

denominator = (
    (N * sumX2 - sumX ** 2) *
    (N * sumY2 - sumY ** 2)
) ** 0.5

# Pearson correlation
r = numerator / denominator

# Regression coefficients
b1 = numerator / (N * sumX2 - sumX ** 2)

b0 = (sumY - b1 * sumX) / N

# Predicted values
Y_pred = [b0 + b1 * x for x in X]

# Residuals
residuals = [
    Y[i] - Y_pred[i]
    for i in range(N)
]

# R-squared
R2 = r ** 2

# SSE
SSE = sum(e ** 2 for e in residuals)

# Standard Error
Syx = (SSE / (N - 2)) ** 0.5

# RMSE
RMSE = (SSE / N) ** 0.5


# --------------------------------------------------
# SPEARMAN RANK CORRELATION
# --------------------------------------------------

def calculate_ranks(values):

    sorted_values = sorted(
        (value, index)
        for index, value in enumerate(values)
    )

    ranks = [0] * len(values)

    i = 0

    while i < len(sorted_values):

        j = i

        while (
            j < len(sorted_values)
            and sorted_values[j][0] == sorted_values[i][0]
        ):
            j += 1

        average_rank = (i + 1 + j) / 2

        for k in range(i, j):
            original_index = sorted_values[k][1]
            ranks[original_index] = average_rank

        i = j

    return ranks


rank_X = calculate_ranks(X)
rank_Y = calculate_ranks(Y)

mean_rank_X = sum(rank_X) / N
mean_rank_Y = sum(rank_Y) / N

numerator_rs = sum(
    (rank_X[i] - mean_rank_X) *
    (rank_Y[i] - mean_rank_Y)
    for i in range(N)
)

denominator_rs = (
    sum((rank - mean_rank_X) ** 2 for rank in rank_X) *
    sum((rank - mean_rank_Y) ** 2 for rank in rank_Y)
) ** 0.5

rs = numerator_rs / denominator_rs


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("📊 Social Media Usage vs Academic Performance")

st.markdown(
    """
    ### 🎓 Statistical Analysis & Predictive Modeling

    This application analyzes the relationship between
    **daily social media screen time** and **academic exam performance**
    using correlation and linear regression.
    """
)

st.divider()


# --------------------------------------------------
# DATASET OVERVIEW
# --------------------------------------------------

st.subheader("📚 Dataset Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("👥 Students", N)

with col2:
    st.metric("📱 X Variable", "Screen Time (hours)")

with col3:
    st.metric("🎓 Y Variable", "Exam Score (%)")

st.divider()


# --------------------------------------------------
# STATISTICAL RESULTS
# --------------------------------------------------

st.subheader("📈 Statistical Results")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Pearson Correlation (r)",
        f"{r:.6f}"
    )

with col2:
    st.metric(
        "Spearman Correlation (rs)",
        f"{rs:.6f}"
    )

with col3:
    st.metric(
        "R²",
        f"{R2:.6f}"
    )

with col4:
    st.metric(
        "R² Percentage",
        f"{R2 * 100:.4f}%"
    )


col5, col6, col7, col8 = st.columns(4)

with col5:
    st.metric(
        "Standard Error (Syx)",
        f"{Syx:.4f}"
    )

with col6:
    st.metric(
        "RMSE",
        f"{RMSE:.4f}"
    )

with col7:
    st.metric(
        "Slope (b₁)",
        f"{b1:.6f}"
    )

with col8:
    st.metric(
        "Intercept (b₀)",
        f"{b0:.6f}"
    )


st.divider()


# --------------------------------------------------
# REGRESSION EQUATION
# --------------------------------------------------

st.subheader("🧮 Linear Regression Model")

st.success(
    f"📌 Regression Equation: "
    f"Y = {b0:.4f} + {b1:.6f}X"
)

st.write(
    "Where:"
)

st.write(
    "🔹 X = Daily social media screen time in hours"
)

st.write(
    "🔹 Y = Predicted academic exam score (%)"
)


st.divider()


# --------------------------------------------------
# PREDICTION
# --------------------------------------------------

st.subheader("🔮 Exam Score Prediction")

st.write(
    "Enter the student's daily social media screen time "
    "to estimate the exam score."
)

hours = st.number_input(
    "📱 Daily Social Media Screen Time (hours)",
    min_value=0.0,
    max_value=24.0,
    value=5.0,
    step=0.5
)

if st.button("🚀 Predict Exam Score"):

    predicted_score = b0 + b1 * hours

    st.success(
        f"🎯 Predicted Exam Score: "
        f"{predicted_score:.2f}%"
    )

    st.info(
        f"📐 Using: Y = {b0:.4f} + {b1:.6f} × {hours}"
    )


st.divider()


# --------------------------------------------------
# SCATTER PLOT
# --------------------------------------------------

st.subheader("📊 Scatter Plot & Regression Line")

fig, ax = plt.subplots(figsize=(10, 5))

ax.scatter(
    X,
    Y,
    label="👨‍🎓 Student Data"
)

# Regression line
Y_line = [
    b0 + b1 * x
    for x in X
]

ax.plot(
    X,
    Y_line,
    label="📈 Regression Line"
)

ax.set_xlabel(
    "Daily Social Media Screen Time (hours)"
)

ax.set_ylabel(
    "Exam Score (%)"
)

ax.set_title(
    "Social Media Usage vs Academic Performance"
)

ax.legend()

ax.grid(True)

st.pyplot(fig)


st.divider()


# --------------------------------------------------
# INTERPRETATION
# --------------------------------------------------

st.subheader("📝 Analysis Summary")

st.write(
    f"""
    🔹 The Pearson correlation coefficient is **{r:.6f}**.

    🔹 The Spearman rank correlation coefficient is **{rs:.6f}**.

    🔹 The coefficient of determination (R²) is
    **{R2:.6f}**, meaning approximately **{R2 * 100:.4f}%**
    of the variation in exam scores is explained by this
    simple linear model for this sample.

    🔹 The standard error of estimate is **{Syx:.4f}**.

    🔹 The RMSE is **{RMSE:.4f}**.

    🔹 The fitted regression model is:

    **Y = {b0:.4f} + {b1:.6f}X**
    """
)


