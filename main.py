import streamlit as st
import pandas as pd
import re

# Sample service data
data = {
    "Service": [
        "Mission Australia",
        "Fake Service 1",
        "Fake Service 2",
        "Fake Service 3",
        "Fake Service 4",
        "Fake Service 5",
        "Fake Service 6",
        "Fake Service 7",
        "Fake Service 8",
        "Fake Service 9",
        "Fake Service 10",
        "Fake Service 11",
        "Fake Service 12",
        "Fake Service 13",
        "Fake Service 14",
        "Fake Service 15",
        "Fake Service 16",
        "Fake Service 17",
        "Fake Service 18",
        "Fake Service 19",
    ],
    "Type": [
        "NGO",
        "Private",
        "Disability",
        "Private",
        "SESLHD",
        "NGO",
        "Private",
        "Disability",
        "Private",
        "SESLHD",
        "NGO",
        "Private",
        "Disability",
        "Private",
        "SESLHD",
        "NGO",
        "Private",
        "Disability",
        "Private",
        "SESLHD",
    ],
    "Eligibility Criteria": [
        "16+ years, Eastern Suburbs Mental Health, St George Mental Health, Sutherland Mental Health, anxiety, depression, eating disorders, substance abuse, mood disorder, schizophrenia",
        "Depression, 16+ years",
        "Physical disability, mental health support",
        "Eating disorders, 16+ years",
        "Substance abuse, 18+ years",
        "16+ years, Eastern Suburbs Mental Health, anxiety",
        "Depression, 18+ years",
        "Physical disability, 18+ years",
        "Eating disorders, 16+ years, St George Mental Health",
        "Substance abuse, 18+ years, Sutherland Mental Health",
        "16+ years, mood disorder",
        "Depression, 18+ years, Eastern Suburbs Mental Health",
        "Physical disability, mental health support, St George Mental Health",
        "Eating disorders, 16+ years, Sutherland Mental Health",
        "Substance abuse, 18+ years, Eastern Suburbs Mental Health",
        "16+ years, schizophrenia, St George Mental Health",
        "Depression, 18+ years, Sutherland Mental Health",
        "Physical disability, 18+ years, Eastern Suburbs Mental Health",
        "Eating disorders, 16+ years, mood disorder",
        "Substance abuse, 18+ years, St George Mental Health",
    ],
    "Catchment Area": [
        "Eastern Suburbs Mental Health",
        "St George Mental Health",
        "Sutherland Mental Health",
        "Sutherland Mental Health",
        "Eastern Suburbs Mental Health",
        "Eastern Suburbs Mental Health",
        "St George Mental Health",
        "Sutherland Mental Health",
        "Sutherland Mental Health",
        "Eastern Suburbs Mental Health",
        "Eastern Suburbs Mental Health",
        "St George Mental Health",
        "Sutherland Mental Health",
        "Sutherland Mental Health",
        "Eastern Suburbs Mental Health",
        "St George Mental Health",
        "Sutherland Mental Health",
        "Eastern Suburbs Mental Health",
        "St George Mental Health",
    "Sutherland Mental Health",
    ],
    "Current Support": [
        "Mental Health Service",
        "GP",
        "Psychiatrist (Private or Public)",
        "Psychologist",
        "Other",
        "Mental Health Service",
        "GP",
        "Psychiatrist (Private or Public)",
        "Psychologist",
        "Other",
        "Mental Health Service",
        "GP",
        "Psychiatrist (Private or Public)",
        "Psychologist",
        "Other",
        "Mental Health Service",
        "GP",
        "Psychiatrist (Private or Public)",
        "Psychologist",
        "Other",
    ]
}

df = pd.DataFrame(data)

#Function to get recommendations
def get_recommendations(age, condition, catchment_area, current_support):
    eligible_services = df[(df["Eligibility Criteria"].str.contains(condition)) & (df["Catchment Area"] == catchment_area) & (df["Current Support"] == current_support)]
    eligible_services = eligible_services[eligible_services["Eligibility Criteria"].apply(lambda x: int(re.search(r"\d+", x).group()) <= age)]
    return eligible_services

#Streamlit app
st.title("Mental Health Service Eligibility and Recommendation Program")

st.subheader("Patient Information")
age = st.number_input("Age", min_value=1, max_value=120, value=25, step=1)
condition = st.selectbox(
    "Condition",
    options=["anxiety", "depression", "schizophenia", "mood disorder", "physical disability", "eating disorders", "substance abuse"],
)
catchment_area = st.selectbox(
    "Catchment Area",
    options=["Eastern Suburbs Mental Health", "St George Mental Health", "Sutherland Mental Health"],
)
current_support = st.selectbox(
    "Current Support",
    options=["Mental Health Service", "GP", "Psychiatrist (Private or Public)", "Psychologist", "Other"],
)

if st.button("Get Recommendations"):
    recommendations = get_recommendations(age, condition, catchment_area, current_support)
    if not recommendations.empty:
        st.write("Recommended services:")
        st.write(recommendations)
    else:
        st.write("No services found for the given criteria.")