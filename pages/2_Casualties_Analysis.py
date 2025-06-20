import streamlit as st
from utils.data_loader import load_common_data

st.title("💔 Casualties Breakdown")

df = load_common_data()
st.image("assets/images/casualty_metrics.png", caption="Passenger and Crew Casualty Breakdown")
st.image("assets/images/casualty_pie.png", caption="Survivor vs. Deaths Pie Chart")

st.subheader("Key Figures")
st.metric("Confirmed Deaths", int(df["Confirmed_Deaths"]))
st.metric("Survivors", int(df["Survivors"]))
st.metric("Survivor Rate (%)", round(df["Survivors"][0] / df["Total_People_Onboard"][0] * 100, 2))
