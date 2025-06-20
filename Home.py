import streamlit as st

st.set_page_config(
    page_title="Air India AI171 Crash Analytics",
    page_icon="✈️",
    layout="wide"
)

st.title("🚨 Air India Flight AI171 Crash Analytics Dashboard")
st.markdown("""
This interactive dashboard presents data insights and emergency response analysis from the tragic crash of AI171.

Explore the navigation sidebar to access:
- **Incident Overview**
- **Casualties Analysis**
- **Emergency Response**
- **Analytics Dashboard**
- **Public Reactions**

Built using **Streamlit**, **matplotlib**, and **pandas** by [Adebayo Olaonipekun](https://www.linkedin.com/in/adebayo-olaonipekun/), this dashboard showcases storytelling through data.

---  
""")
st.image("assets/images/casualty_pie.png", caption="Victim and Survivor Breakdown")
