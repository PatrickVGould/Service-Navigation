import streamlit as st
import pandas as pd
import re

# Sample service data
data = {
    "Service": [
        "Mission Australia",
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
        "16+ years, Eastern Suburbs Mental Health, St George Mental Health, Sutherland Mental Health, anxiety, depression, eating disorders, substance abuse, mood disorder, schizophrenia",
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
        eligible_services["Eligibility Criteria"].apply(lambda x: int(re.search(r"\d+", x).group()) <= age)
    ]
    return eligible_services


# Streamlit app
st.title("Mental Health Service Eligibility and Recommendation Program")

st.subheader("Patient Information")
age = st.number_input("Age", min_value=1, max_value=120, value=25, step=1)
condition = st.selectbox(
    "Condition",
    options=["anxiety", "depression", "schizophenia", "mood disorder", "physical disability", "eating disorders", "substance abuse"],)
catchment_area = st.selectbox(
    "Catchment Area",
    options=["Eastern Suburbs Mental Health", "St George Mental Health", "Sutherland Mental Health"],
)
current_support = st.selectbox(
    "Current Support",
    options = ["Mental Health Service", "GP", "Psychiatrist (Private or Public)", "Psychologist", "Other"],

if st.button("Get Recommendations"):
    recommendations = get_recommendations(age, condition)
    if not recommendations.empty:
        st.write("Recommended services:")
        st.write(recommendations)
    else:
        st.write("No services found for the given criteria.")
