import streamlit as st
import pandas as pd

# Sample service data
data = {
    "Service": [
        "Service A",
        "Service B",
        "Service C",
        "Service D",
        "Service E",
    ],
    "Type": [
        "NGO",
        "Private",
        "Disability",
        "Private",
        "NGO",
    ],
    "Eligibility Criteria": [
        "18+ years, anxiety",
        "Depression, 16+ years",
        "Physical disability, mental health support",
        "Eating disorders, 16+ years",
        "Substance abuse, 18+ years",
    ],
}

df = pd.DataFrame(data)

# Function to get recommendations
def get_recommendations(age, condition):
    eligible_services = df[df["Eligibility Criteria"].str.contains(condition)]
    eligible_services = eligible_services[
        eligible_services["Eligibility Criteria"].str.contains(f"{age}+ years")
    ]
    return eligible_services

# Streamlit app
st.title("Mental Health Service Eligibility and Recommendation Program")

st.subheader("Patient Information")
age = st.number_input("Age", min_value=1, max_value=120, value=25, step=1)
condition = st.selectbox(
    "Condition",
    options=["anxiety", "depression", "physical disability", "eating disorders", "substance abuse"],
)

if st.button("Get Recommendations"):
    recommendations = get_recommendations(age, condition)
    if not recommendations.empty:
        st.write("Recommended services:")
        st.write(recommendations)
    else:
        st.write("No services found for the given criteria.")
