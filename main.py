import streamlit as st
import pandas as pd
import re

# Sample service data
data = {
    "Service": [
        "Mission Australia",
        "Hope Horizon",
        "Nurture Now",
        "New Heights Support",
        "Brighter Pathways",
        "Mindful Moments",
        "Compassionate Care",
        "Empowerment Alliance",
        "Heart and Hand Support",
        "Serene Steps",
        "Harmony House",
        "Rays of Light Support",
        "Guiding Stars",
        "Safe Haven Services",
        "Peaceful Minds Support",
        "Horizon Help",
        "Mindful Mediation",
        "Hopeful Hearts Support",
        "Caring Connections",
        "Wonderful Workers"
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
        "16+ years, Eastern Suburbs Mental Health, Anxiety, Depression, Eating disorders, Substance abuse, Mood disorder, Schizophrenia",
        "Depression, 16+ years",
        "Physical disability, Substance abuse, mental health support",
        "Eating disorders, Mood disorder, Physical disability 16+ years",
        "Substance abuse, Mood disorder, 18+ years",
        "16+ years, Eating disorders, Anxiety, Depression",
        "Depression, Substance abuse, Mood disorder, 18+ years",
        "Physical disability, Schizophrenia, 18+ years",
        "Eating disorders, 16+ years",
        "Substance abuse, Eating disorders, 18+ years",
        "16+ years, Eating disorders, Mood disorder",
        "Depression, Eating disorders, Mood disorder, 18+ years",
        "Physical disability, mental health support",
        "Eating disorders, 16+ years",
        "Substance abuse, 18+ years, Mood disorder",
        "16+ years, Substance abuse, Schizophrenia",
        "Depression, 18+ years",
        "Physical disability, Schizophrenia, 18+ years",
        "Eating disorders, 16+ years, Schizophrenia, Mood disorder",
        "Substance abuse, Schizophrenia, 18+ years",
    ],
    "Catchment Area": [
        "Eastern Suburbs Mental Health, St George Mental Health, Sutherland Mental Health",
        "St George Mental Health",
        "Sutherland Mental Health, Eastern Suburbs Mental Health",
        "Sutherland Mental Health",
        "Eastern Suburbs Mental Health, St George Mental Health, Sutherland Mental Health",
        "Eastern Suburbs Mental Health",
        "St George Mental Health",
        "Sutherland Mental Health, Eastern Suburbs Mental Health",
        "Sutherland Mental Health, St George Mental Health",
        "Eastern Suburbs Mental Health",
        "Eastern Suburbs Mental Health",
        "St George Mental Health, Sutherland Mental Health",
        "Sutherland Mental Health",
        "Sutherland Mental Health",
        "Eastern Suburbs Mental Health",
        "St George Mental Health",
        "Sutherland Mental Health, Eastern Suburbs Mental Health",
        "Eastern Suburbs Mental Health, St George Mental Health, Sutherland Mental Health",
        "St George Mental Health",
    "Sutherland Mental Health",
    ],
    "Current Support": [
        "Mental Health Service, GP, Psychiatrist (Private or Public), Psychologist, Other",
        "Mental Health Service, GP, Psychiatrist (Private or Public), Psychologist, Other",
        "Mental Health Service, GP, Psychiatrist (Private or Public), Psychologist, Other",
        "Mental Health Service, GP, Psychiatrist (Private or Public), Psychologist, Other",
        "Mental Health Service, GP, Psychiatrist (Private or Public), Psychologist, Other",
        "Mental Health Service, GP, Psychiatrist (Private or Public), Psychologist, Other",
        "Mental Health Service, GP, Psychiatrist (Private or Public), Psychologist, Other",
        "Mental Health Service, GP, Psychiatrist (Private or Public), Psychologist, Other",
        "Mental Health Service, GP, Psychiatrist (Private or Public), Psychologist, Other",
        "Mental Health Service, GP, Psychiatrist (Private or Public), Psychologist, Other",
        "Mental Health Service, GP, Psychiatrist (Private or Public), Psychologist, Other",
        "Mental Health Service, GP, Psychiatrist (Private or Public), Psychologist, Other",
        "Mental Health Service, GP, Psychiatrist (Private or Public), Psychologist, Other",
        "Mental Health Service, GP, Psychiatrist (Private or Public), Psychologist, Other",
        "Mental Health Service, GP, Psychiatrist (Private or Public), Psychologist, Other",
        "Mental Health Service, GP, Psychiatrist (Private or Public), Psychologist, Other",
        "Mental Health Service, GP, Psychiatrist (Private or Public), Psychologist, Other",
        "Mental Health Service, GP, Psychiatrist (Private or Public), Psychologist, Other",
        "Mental Health Service, GP, Psychiatrist (Private or Public), Psychologist, Other",
        "Mental Health Service, GP, Psychiatrist (Private or Public), Psychologist, Other",
    ]
}

df = pd.DataFrame(data)

fake_urls = [f"http://www.example.com/{name.lower().replace(' ', '-')}" for name in data["Service"]]
df["URL"] = fake_urls

#Function to get recommendations
def get_recommendations(age, condition, catchment_area, current_support):
    eligible_services = df[
        (df["Eligibility Criteria"].str.contains(condition, case=False)) &
        (df["Catchment Area"].str.contains(catchment_area, case=False)) &
        (df["Current Support"].str.contains(re.escape(current_support), case=False))
    ]
    eligible_services = eligible_services[
        eligible_services["Eligibility Criteria"].apply(
            lambda x: int(re.search(r"\d+", x).group()) <= age if re.search(r"\d+", x) else False
        )
    ]
    return eligible_services if not eligible_services.empty else pd.DataFrame()

#Streamlit app
st.set_page_config(page_title='MH Service Eligibility')

st.title("Mental Health Service Eligibility and Recommendation Program")

st.subheader("Patient Information")
age = st.number_input("Age", min_value=1, max_value=120, value=25, step=1)

st.subheader("Condition")
condition_options = [
    "anxiety",
    "depression",
    "schizophrenia",
    "mood disorder",
    "physical disability",
    "eating disorders",
    "substance abuse",
]
selected_conditions = [option for option in condition_options if st.checkbox(option, key=option)]

st.subheader("Catchment Area")
catchment_area = st.selectbox(
    "Catchment Area",
    options=["Eastern Suburbs Mental Health", "St George Mental Health", "Sutherland Mental Health"],
)

st.subheader("Current Support")
current_support_options = [
    "Mental Health Service",
    "GP",
    "Psychiatrist (Private or Public)",
    "Psychologist",
    "Other",
]
selected_current_support = [option for option in current_support_options if st.checkbox(option, key='cs_'+option)]

if st.button("Get Recommendations"):
    recommendations_list = []
    for condition in selected_conditions:
        for current_support in selected_current_support:
            temp = get_recommendations(age, condition, catchment_area, current_support)
            if not temp.empty:
                recommendations_list.append(temp)

    recommendations = pd.concat(recommendations_list).drop_duplicates().reset_index(drop=True)

    if not recommendations.empty:
        st.write("Recommended services:")
        for i in range(len(recommendations)):
            service = recommendations.iloc[i]
            st.markdown(f"**Service {i+1}: {service['Service']}**")
            st.write(f"**Eligibility Criteria:** *{service['Eligibility Criteria']}*")
            st.write(f"**Catchment Area:** *{service['Catchment Area']}*")
            st.write(f"**Current Support Required:** *{service['Current Support']}*")
            st.write(f"URL: {service['URL']}")
            st.markdown("""---""")
    else:
        st.write("No services found for the given criteria.")

